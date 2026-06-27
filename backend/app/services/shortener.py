from app.utils.generator import generate_short_code

# Temporary storage (Phase 1 only)
links = {}


def create_short_url(original_url: str) -> str:
    while True:
        short_code = generate_short_code()

        if short_code not in links:
            break

    links[short_code] = original_url

    return short_code

def get_original_url(short_code: str):

    return links.get(short_code)