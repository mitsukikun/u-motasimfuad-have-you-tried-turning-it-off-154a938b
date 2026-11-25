"""Write one funny line from a hopeless tech support agent to a desperate customer."""

LINE = "Don't panic — your wedding photos are only mostly gone. Have you tried turning it off and on again? Honestly, that's my entire plan."

try:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
except OSError:
    pass
