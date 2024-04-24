import re


class PhoneNumberExtractor:
    def __init__(self, page_text):
        self.page_text = page_text
        self.regex_patterns = [
            r"[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\.\0-9]*(?=[^0-9])",
            r"(\+\d{1,2}\s?\(\d{3,}\)\s?\d{2,}[-\s]?\d{2,}[-\s]?\d{2,})",
            r"\(?\d{2}\)?\s?\d{4,5}-\d{4}|\+\d{2}\s?\d{2}\s?\d{4,5}-\d{4}",
            r"\(?\d{3}\)?\s?\d{3}-\d{4}|\+\d{1}\s?\d{3}\s?\d{3}-\d{4}",
        ]

    def extract_phone_numbers(self):
        numbers = []
        for text in self.page_text:
            for regex in self.regex_patterns:
                phone_pattern = re.compile(regex)
                phone_numbers = phone_pattern.findall(text)
                if phone_numbers:
                    numbers = numbers + phone_numbers
        return numbers


class PhoneNumbersFilter:
    def __init__(self, phone_numbers):
        self.phone_numbers = phone_numbers

    def filter_numbers(self):
        numbers = []
        filtered_numbers = []

        for number in self.phone_numbers:
            clean_number = re.sub(r"[^\d+()\s]", "", number).strip()
            if len(clean_number.strip()) > 5:
                numbers.append(clean_number)

        for phone1 in numbers:
            is_subset = False
            for phone2 in numbers:
                if phone1 != phone2 and phone1 in phone2:
                    is_subset = True
                    break
            if not is_subset:
                filtered_numbers.append(phone1)
        return filtered_numbers
