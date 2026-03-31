with open('index_v019_Board_right_click_Fixed.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update .glass-panel to use the new var(--glass-blur) format
search = """    /* Glass Panels */
    .glass-panel {
        background: var(--glass-surface);
        backdrop-filter: blur(var(--glass-blur));
        -webkit-backdrop-filter: blur(var(--glass-blur));
        border: 1px solid var(--glass-border);
        box-shadow: var(--glass-highlight), var(--glass-shadow);
        border-radius: var(--radius-lg);
    }"""
replace = """    /* Glass Panels */
    .glass-panel {
        background: var(--glass-surface);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);
        border: 1px solid var(--glass-border-strong);
        box-shadow: var(--glass-highlight), var(--glass-shadow);
        border-radius: var(--radius-lg);
        position: relative;
        overflow: hidden;
    }

    /* Diagonal Reflection for Glass */
    .glass-panel::before, .modal-box::before, .details-panel::before {
        content: '';
        position: absolute;
        top: 0; left: -100%; width: 50%; height: 100%;
        background: linear-gradient(120deg, transparent, rgba(255, 255, 255, 0.05), transparent);
        transform: skewX(-25deg);
        pointer-events: none;
        z-index: 10;
        animation: glassSweep 10s infinite cubic-bezier(0.25, 1, 0.5, 1);
    }"""
content = content.replace(search, replace)

search_anims = """    /* Animations */
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    @keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
    @keyframes pulseGlow { 0% { box-shadow: 0 0 5px var(--accent-glow); } 50% { box-shadow: 0 0 15px var(--accent-glow); } 100% { box-shadow: 0 0 5px var(--accent-glow); } }"""
replace_anims = """    /* Animations */
    @keyframes fadeIn { from { opacity: 0; filter: blur(10px); } to { opacity: 1; filter: blur(0); } }
    @keyframes slideUp { from { transform: translateY(30px) scale(0.98); opacity: 0; filter: blur(5px); } to { transform: translateY(0) scale(1); opacity: 1; filter: blur(0); } }
    @keyframes pulseGlow { 0% { box-shadow: 0 0 5px var(--accent-glow); } 50% { box-shadow: 0 0 20px var(--accent-glow); } 100% { box-shadow: 0 0 5px var(--accent-glow); } }
    @keyframes glassSweep { 0% { left: -100%; } 20% { left: 200%; } 100% { left: 200%; } }

    /* Panel Transition Animation */
    .animate-liquid-reveal {
        animation: liquidReveal 0.6s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    }
    @keyframes liquidReveal {
        0% { opacity: 0; transform: scale(0.98) translateY(10px); backdrop-filter: blur(0px) saturate(100%); }
        100% { opacity: 1; transform: scale(1) translateY(0); backdrop-filter: var(--glass-blur); }
    }"""
content = content.replace(search_anims, replace_anims)

# Fix other blur() references that now use the string directly
search_details = """    .details-panel {
        width: 350px;
        flex-shrink: 0;
        background-color: var(--glass-surface);
        backdrop-filter: blur(var(--glass-blur));
        -webkit-backdrop-filter: blur(var(--glass-blur));"""
replace_details = """    .details-panel {
        width: 350px;
        flex-shrink: 0;
        background-color: var(--glass-surface);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);"""
content = content.replace(search_details, replace_details)

search_dash = """    .dash-card {
        background: var(--glass-surface);
        backdrop-filter: blur(var(--glass-blur));
        -webkit-backdrop-filter: blur(var(--glass-blur));"""
replace_dash = """    .dash-card {
        background: var(--glass-surface);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);"""
content = content.replace(search_dash, replace_dash)

search_toolbar = """    /* --- TOOLBAR --- */
    .toolbar-container {
        display: flex; flex-wrap: wrap; gap: 10px; align-items: center; padding: 10px 14px;
        background: var(--glass-surface); border: 1px solid var(--glass-border);
        backdrop-filter: blur(var(--glass-blur));
        -webkit-backdrop-filter: blur(var(--glass-blur));"""
replace_toolbar = """    /* --- TOOLBAR --- */
    .toolbar-container {
        display: flex; flex-wrap: wrap; gap: 10px; align-items: center; padding: 10px 14px;
        background: var(--glass-surface); border: 1px solid var(--glass-border-strong);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);"""
content = content.replace(search_toolbar, replace_toolbar)

search_tab = """    .tab.active {
        background: var(--glass-surface); color: #fff;
        border-color: var(--glass-border); border-bottom-color: transparent;
        box-shadow: var(--glass-highlight), 0 -4px 12px rgba(0,0,0,0.15);
        backdrop-filter: blur(var(--glass-blur)); -webkit-backdrop-filter: blur(var(--glass-blur));
    }"""
replace_tab = """    .tab.active {
        background: var(--glass-surface); color: #fff;
        border-color: var(--glass-border-strong); border-bottom-color: transparent;
        box-shadow: var(--glass-highlight), 0 -8px 20px rgba(0,0,0,0.2);
        backdrop-filter: var(--glass-blur); -webkit-backdrop-filter: var(--glass-blur);
        z-index: 10;
        transform: scale(1.02);
        transform-origin: bottom center;
    }"""
content = content.replace(search_tab, replace_tab)

search_board = """    .board-card {
        background: var(--glass-surface);
        backdrop-filter: blur(var(--glass-blur));
        -webkit-backdrop-filter: blur(var(--glass-blur));"""
replace_board = """    .board-card {
        background: var(--glass-surface);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);"""
content = content.replace(search_board, replace_board)

with open('index_v019_Board_right_click_Fixed.html', 'w', encoding='utf-8') as f:
    f.write(content)
