#! /bin/python3

from pkg.pigeon import Locker, Unlocker, Injector, Extractor, Authentication, PolyglotWrapper
from pkg.util import discover_all_files, show_banner, select_files_by_index, Color, colorize, update_tools
from pkg.config import INTER_REP_NAME, DEF_OUTPUT_PATH, DEF_PASSWORD 
import sys, os


show_banner()
print(f"""{Color.BLUE}SELECT A OPTION :

		{Color.BOLD}[1]. Hide files
		[2]. Extract files
		[3].Update Script
		[4].exit
        {Color.RESET}
{Color.RESET}""")

try:
    option = int(input("\n>"))
except EOFError:
    sys.exit()

if option == 1 or option == 2:
    cover_image = input(
            f"""
            {Color.MAGENTA}COVER_IMAGE is a JPEG or PNG image where the file(s) will be obscured or extracted
            {Color.YELLOW}{Color.BOLD}
            Enter the path of the cover image :
            >{Color.RESET}"""
                        )
    if not cover_image:
        print(f"{Color.RED}{Color.BOLD}Cover Image not found!{Color.RESET}")
        sys.exit()

    if option == 1:
        dirs = input(f"""
            {Color.MAGENTA}DIRECTORY that contains all files to be obscured.
            No other files should keep in the DIRECTORY not to be hidden.
            {Color.YELLOW}{Color.BOLD}
            Enter the directory path to be hidden :
            >{Color.RESET}"""
                     )
        if not dirs:
            print(f"{Color.RED}{Color.BOLD}Directory not found!{Color.RESET}")
            sys.exit()

        all_files = discover_all_files(dirs)
        if not all_files:
            print(
                    colorize(
                        "No content found!",
                        Color.BG_RED
                        )
                    )
            sys.exit()

        print(f"""
            {Color.MAGENTA}Select file(s) by index number separated by space to hide.
            If all files need to be hidden , enter '*'
            {Color.YELLOW}{Color.BOLD}
        """)
        files = select_files_by_index(all_files)
        password = input(f"""
            {Color.MAGENTA}PASSWORD is strong feature to save obscured file(s) from leaking to the imposter(s)
            {Color.YELLOW}{Color.BOLD}
            Enter a strong password (at least 8 characters) : 
            >{Color.RESET}""")
        if not password:
            print(f"{Color.RED}{Color.BOLD}Password not found!{Color.RESET}")
            print(colorize("Using default password!", Color.YELLOW))
            password = DEF_PASSWORD

        Auth = Authentication(password=password)
        Locker(INTER_REP_NAME, Auth.get_hash(), True, *files)
        Injector(cover_image, INTER_REP_NAME)
        
        polyglot = input(
        colorize("Use wrapper for evading compression? (y/n)",Color.YELLOW)
                 )

        if polyglot.lower() == "y":
            wrapper = PolyglotWrapper(cover_image,".docx")
            wrapper.conceal()
            print(
                    colorize(f"container wrapped into {wrapper.fname}!",Color.YELLOW)
                    )
            sys.exit()



        print(f"{Color.GREEN}{Color.BOLD}File(s) successfully injected into '{cover_image}'{Color.RESET}")

    elif option == 2:
        password = input(f"""
            {Color.MAGENTA}PASSWORD is a crucial things to extract files , set during obscuration.
            {Color.YELLOW}{Color.BOLD}
            Enter the password to extract file(s) :  
            >{Color.RESET}""")
        
        if not password:
            print(f"{Color.RED}{Color.BOLD}Password not found!{Color.RESET}")
            password = DEF_PASSWORD
        outputpath = input(f"""
            {Color.MAGENTA}OUTPUT_PATH is a path where the extracted file(s) will be saved.
            {Color.YELLOW}{Color.BOLD}
            Enter the output path : 
            >{Color.RESET}""")

        if not outputpath:
            outputpath = DEF_OUTPUT_PATH

        Auth = Authentication(password=password)
        Extractor(cover_image, INTER_REP_NAME)

        u = Unlocker(
                zipfile_name=INTER_REP_NAME, key=Auth.get_hash(),
                output_path=outputpath
                )
        if not u.status:
            print(
                    colorize("Invalid password!\n", Color.BG_RED),
                    colorize("file could not be extracted!",Color.RED)
                    )
            os.remove(outputpath)
            sys.exit()

        print(f"{Color.GREEN}{Color.BOLD}File successfully extracted to '{u.output_path}'{Color.RESET}")

    elif option == 3:
        update_tools()


