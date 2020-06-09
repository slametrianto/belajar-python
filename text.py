def create_html(tag, text):
    html = f"<{tag}>{text}</{tag}>"
    return html

    html = create_html("P", "hello python")
    print(html)