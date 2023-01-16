import json

stickers = {
    'сука': 'CAACAgIAAxkBAAEEcaRjqcXPuUPCsZJl5lQoj77EH8mJ4wACZBcAAnHMfRiNj8NSSqwBfx4E',
    'заебался': 'CAACAgIAAxkBAAEEcaZjqcXgpDbObPuffngAAW-hmLye7dsAAmkXAAJxzH0YBPzF5hwjLrweBA',
    'csb': 'CAACAgIAAxkBAAED-otjH1RHVIOAY5yYd964CZ62YEialwACyAMAAuB5Ugf5pW2ZGcswwB4E', # CoolStoryBob
    'linkannoy': 'CAACAgEAAxkBAAED-oxjH1TFRPcEmdHX9tYryHEgZ_1EdgACuAIAAmv_ag-ry1qRfwZrYx4E', # Annoyed Link
    'wtf': 'CAACAgIAAxkBAAED-o5jH1UbfNJummkwk5I5tZmDv0qr9gACCAEAAqb6-iDY6ISR4F1YCx4E', # WTF Dante
    'втф': 'CAACAgIAAxkBAAED-o5jH1UbfNJummkwk5I5tZmDv0qr9gACCAEAAqb6-iDY6ISR4F1YCx4E', # WTF Dante
    'KEKW': 'CAACAgIAAxkBAAED-o9jH1VQOyTXQUI9ZvEpAVx5o_1eWwACEg0AAmnM4Usk2QhpG7xijB4E',
    'кекв': 'CAACAgIAAxkBAAED-o9jH1VQOyTXQUI9ZvEpAVx5o_1eWwACEg0AAmnM4Usk2QhpG7xijB4E',
    'tfd': 'CAACAgIAAxkBAAED-pBjH1Vjdfmm2TyzZHE8zkc9FHlZVQACTBcAAp8t4Et20VjBp0x_0x4E',
    'тфд': 'CAACAgIAAxkBAAED-pBjH1Vjdfmm2TyzZHE8zkc9FHlZVQACTBcAAp8t4Et20VjBp0x_0x4E',
    'cry': 'CAACAgIAAxkBAAED-pFjH1V1vkqPKGBjcBzvNQjHhpxFvgACjBgAAkisYEgZdb0fMLAa4x4E', # crying emoji
    'ura': 'CAACAgIAAxkBAAED-pJjH1WH5gz7j0nbOQuqK2OpuJVvbwACCQwAAg8wwEpENQJd-JigcB4E',
    'ура': 'CAACAgIAAxkBAAED-pJjH1WH5gz7j0nbOQuqK2OpuJVvbwACCQwAAg8wwEpENQJd-JigcB4E',
    'зубки': 'CAACAgQAAxkBAAED-pNjH1WZbDSOps5NSIrnfh8PlLEgJQACpgsAAvc9cFKyhVfvZ0i6sR4E',
    'linkfury': 'CAACAgEAAxkBAAED-pRjH1Wvqb72Jwjrz9eEsq5uvRbehwACxgIAAmv_ag_90w1CQCZkPh4E', # Furious Link
    'linkrly': 'CAACAgEAAxkBAAED-pVjH1XCYKxCAZk5qO0_63niyg_lqAAC0AEAAmv_ag8Vt-tSTsfXTR4E', # Tired Link
    'linkangry': 'CAACAgEAAxkBAAED-pZjH1XQFzmBJRehJbPexyy91I7P_AACxgIAAmv_ag_90w1CQCZkPh4E', # Angry Link
    'linkcrap': 'CAACAgEAAxkBAAED-pdjH1Xh48xOT9hLo6h_sO-aRtelDwACxAIAAmv_ag-Sp0SVsomcdh4E', # Annoyed Link 2
    'linkdamn': 'CAACAgEAAxkBAAED-phjH1YGdCA3Wmtyb5oGkU8cNaTEEQACygIAAmv_ag_XEBrKLd-Z7h4E', # Annoyed Link 3
    'linkcool': 'CAACAgEAAxkBAAED-pljH1Ya_BV_wpe7eInYG0GYNDPeggACVgEAAmv_ag9wKV8AAQ2dy78eBA', # Happy Link
    'eblo': 'CAACAgIAAxkBAAED-ppjH1YxvwH2QZuu9EEe2gI2ZAmjlAACAgADxIsdFfIV2-W3v3I9HgQ',
    'ебло': 'CAACAgIAAxkBAAED-ppjH1YxvwH2QZuu9EEe2gI2ZAmjlAACAgADxIsdFfIV2-W3v3I9HgQ',
    # 'WTF': 'CAACAgEAAxkBAAED-ptjH1ZORFpoeDCxl_aWCXhV3JwTOwACrgIAAhCtywSrY5IfUHKEvx4E', # Scared Vergil
    'oklol': 'CAACAgEAAxkBAAED-pxjH1ZatoteVf-QtN_DDm6TmvuRowACrwIAAhCtywQC7Y9CZ8ACfR4E', # Buscemi Vergil
    'nero': 'CAACAgEAAxkBAAED-p1jH1Z7seoSUOTUlcCOa-MC3VnbeAACSQIAAhCtywTQN0Aodt1hox4E', # Shouting Nero
    'я иду пить чай': 'CAACAgIAAxkBAAEEcXZjqcK_anoIKUt6PH7PRGQfeGDBOgACuBYAAuwYQEhtI8emJHKqAR4E', #Валерий идёт пить чай
    'не ну ахуеть теперь': 'CAACAgIAAxkBAAEEcXhjqcNL74GOHeniKHOW6TPrEGw1XgACOBgAApb4SEgtw5PKKUMiJR4E', #Неро в ахуе уходит
    'ну ахуеть теперь': 'CAACAgIAAxkBAAEEcXhjqcNL74GOHeniKHOW6TPrEGw1XgACOBgAApb4SEgtw5PKKUMiJR4E', #Same as previous
    'не интересует': 'CAACAgIAAxkBAAEEcXpjqcOGPf_qrOkJPx0m0fPLoyQl8wACDhwAAv-eQEgo5hALFxeQdh4E', #Данте в мекиканской шляпи
    'да блять': 'CAACAgIAAxkBAAEEcXxjqcOhXgmxWloVtPpKkkaZ3p93KgACMhoAAhV2WEhu1_aNDXbgcx4E', #Неро рейджит
    'интересует': 'CAACAgIAAxkBAAEEcYBjqcPFouH7DwS4lcCnf3IvhOnoawACSxwAAq_vWEj17w-jIQfklh4E', #Валерий без шляпи
    'абсолютно похуй': 'CAACAgIAAxkBAAEEca5jqcYbC1psJdKEBRc_C1j808OPIgACehcAAnHMfRhuLLYBigZ7YB4E',
    'похуй': 'CAACAgIAAxkBAAEEcYRjqcPw-uiXk7DO6Kdix6I2zXhRZwACIh0AAq6dWEi9HEaVOoRxKx4E', #V пафосно седеет
    'да ну его нахуй': 'CAACAgIAAxkBAAEEcYZjqcQAAQqBxhZ-yJPaEolMsKIB5XoAAhkeAAIeg2BIXjM1PyrtgKQeBA', #Неро по съёбам
    'да ну нахуй': 'CAACAgIAAxkBAAEEcYZjqcQAAQqBxhZ-yJPaEolMsKIB5XoAAhkeAAIeg2BIXjM1PyrtgKQeBA', # Same as previous
    'чего нахуй': 'CAACAgIAAxkBAAEEcYhjqcRPaTvq0w6tjCzOVFm_BQ_mQwACzhcAAltZYEh1HUH7jQSDfB4E', # Same as previous
    'че нахуй': 'CAACAgIAAxkBAAEEcYhjqcRPaTvq0w6tjCzOVFm_BQ_mQwACzhcAAltZYEh1HUH7jQSDfB4E', # Неро в ахуе приходит
    'кринж': 'CAACAgIAAxkBAAEEcYpjqcSApXym9OLR-9lq8KpzQU52sgACWBsAAtzPWUiHXz5LgtsiJh4E', #Nero fucking dies
    'понял спасибо': 'CAACAgIAAxkBAAEEcYxjqcSaIwd9RMJqMBxXAAGM7516H68AAsEdAAI0_mhIkruIAWRyIdIeBA',
    'удачи попуск': 'CAACAgIAAxkBAAEEcZBjqcTqzWRiu2j458NUs4EWcZjIBQACRRYAAi_BcEi-r1erSA-pox4E',
    'я тоже': 'CAACAgIAAxkBAAEEcZJjqcT5cHhoVugmNbgTt2vXdcwJFAACEhgAAlDucUg_om9Bzb4BhB4E',
    'маме своей так скажешь': 'CAACAgIAAxkBAAEEcZRjqcUGfpU2JXoaVUQIhipRVyoAACLRoAAmKIeEhFSYfrD0LGah4E',
    'молчать чурка': 'CAACAgIAAxkBAAEEcZZjqcUY6LMXOcIIEuEEJ8O4fLVn9QACrRsAAnaIgUiSQJVIvcPdfR4E',
    'жиза': 'CAACAgIAAxkBAAEEcZhjqcUrQsTRfJM2t0mrolMZ7Fa7LQAC-hgAApn3mUioMk85GI4OuR4E',
    'че закибербуллили': 'CAACAgIAAxkBAAEEcZpjqcU2gLZBMZhmaPxuFWLmvZbcqQAC2xYAAmVdyEhbAYJkIQ_STx4E',
    'хуя ты ебать': 'CAACAgIAAxkBAAEEcaBjqcWuJBsRik_ohFADGtxcKc6cagACWRcAAnHMfRjfuzpM4hf9xR4E',
    'нормально так': 'CAACAgIAAxkBAAEEcZxjqcVmFG1jsm5RzR4veRHExdSDygACNhcAAnHMfRjmYIpWMX17yh4E',
    'не работает нихуя': 'CAACAgIAAxkBAAEEcZ5jqcWaxmoH0vkAAa5UFDp6DwwzjwEAAj0XAAJxzH0YSJzY5eK9WMweBA',
    'ну это стадия уже': 'CAACAgIAAxkBAAEEcaJjqcXISAtZsX6ZSl-mI8l3emrx_QACYRcAAnHMfRhVGPyHXjehgB4E',
    'как же это сука пиздато': 'CAACAgIAAxkBAAEEcahjqcX0qzrnY3X9WzAloVdpAZbczAACcBcAAnHMfRivyym2dAUHjB4E',
    'ладно': 'CAACAgIAAxkBAAEEcapjqcYAAZt6-drJj0yyzfSv7dIbpI0AAnYXAAJxzH0Y7QVI_A0YtQMeBA',
    'ага': 'CAACAgIAAxkBAAEEcaxjqcYMZqEQ4fbbMHoVWD374wJS_AACeRcAAnHMfRj_Ou1lD5PpTB4E',
}


# def stickers():
#     out_file = open("stickers.json")
#     return json.load(out_file)

