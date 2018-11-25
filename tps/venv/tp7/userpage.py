html = """
        <!DOCTYPE html>
            <head>
                <title>Mon programme</title>
            </head>
            <body>
                <h3>User page</h3>
                <form action="/logout.py" method="post">
                    <input type="submit" name="send" value="Logout">
                </form>
            </body>
        </html>"""
print("Content-type: text/html; charset=utf-8\n")
print(html)
