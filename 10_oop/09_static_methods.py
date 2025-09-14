class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = " milk, sugar, ginger, cardamom, tea leaves "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)