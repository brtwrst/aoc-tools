import re

re_main = re.compile(r'(?s)<main>\n<article><p>(.*)</p></article>\n</main>')

def parse_website(raw):
    if not raw.startswith('<!DOCTYPE html>'):
        return 'ERROR: No HTML Received'
    main_part = re_main.search(raw)

    if not main_part:
        return 'ERROR: No main part in website'

    main_text = main_part.group(1)

    if main_text.startswith("That's the right answer"):
        return 'SUCCESS - Answer accepted'

    if main_text.startswith('You gave an answer too recently'):
        time = re.search(r'(?:(\d+)m )?(?:(\d+)s)', main_text)
        minutes, seconds = time.groups()
        return f'ERROR: Cooldown {minutes if minutes else 0}m {seconds}s'

    if main_text.startswith("That's not the right answer"):
        reason = re.search(r'your answer is too (\w*)', main_text)
        return 'WRONG ANSWER:' + (f' - Too {reason.group(1)}' if reason else '')

    if main_text.startswith("You don't seem to be solving the right level"):
        return 'ERROR: Already solved'

    return None
