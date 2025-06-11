from django.shortcuts import render
from word2number import w2n

unit_multipliers = {
    "lakh": 1e5,
    "lakhs": 1e5,
    "crore": 1e7,
    "crores": 1e7,
    "million": 1e6,
    "millions": 1e6,
    "billion": 1e9,
    "billions": 1e9
}

def words_to_number(text):
    text = text.lower()
    for unit in unit_multipliers:
        if unit in text:
            number_part = text.replace(unit, "").strip()
            try:
                base = w2n.word_to_num(number_part)
                return int(base * unit_multipliers[unit])
            except ValueError:
                return "Invalid number words."
    try:
        return w2n.word_to_num(text)
    except ValueError:
        return "Invalid input."

def index(request):
    result = None
    if request.method == 'POST':
        text = request.POST.get('number_words')
        number = words_to_number(text)

        if isinstance(number, int):  # Only format if it's a valid number
            # Format using Indian format for crore/lakh style:
            if 'lakh' in text.lower() or 'crore' in text.lower():
                import locale
                locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
                result = locale.format_string("%d", number, grouping=True)
            else:
                # Use western format (e.g., million/billion)
                result = "{:,}".format(number)
        else:
            result = number  # Show the error message

    return render(request, 'converter/index.html', {'result': result})
