with open('index_v019_Board_right_click_Fixed.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Enhance login modal specifically to really show off the glass
login_search = """                    <form onSubmit={handleLogin} className="glass-panel p-10 w-full max-w-sm text-center rounded-2xl"> """
login_replace = """                    <form onSubmit={handleLogin} className="glass-panel p-10 w-full max-w-sm text-center rounded-2xl shadow-2xl animate-liquid-reveal relative">
                        <div className="absolute inset-0 bg-gradient-to-tr from-white/5 to-transparent pointer-events-none rounded-2xl"></div>"""
content = content.replace(login_search, login_replace)

with open('index_v019_Board_right_click_Fixed.html', 'w', encoding='utf-8') as f:
    f.write(content)
