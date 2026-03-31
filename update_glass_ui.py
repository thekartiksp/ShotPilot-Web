import re

with open('index_v019_Board_right_click_Fixed.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update :root variables to be more intense Apple glass
root_search = """    :root {
        --glass-surface: rgba(40, 40, 40, 0.45);
        --glass-border: rgba(255, 255, 255, 0.08);
        --glass-highlight: inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
        --glass-shadow: 0 4px 24px -4px rgba(0, 0, 0, 0.5);
        --glass-active: rgba(255, 255, 255, 0.05);
        --glass-hover: rgba(60, 60, 60, 0.6);
        --glass-blur: 24px;
        --accent-orange: #fa9400;
        --accent-glow: rgba(250, 148, 0, 0.4);
        --text-primary: #f5f5f7;
        --text-secondary: #a1a1a6;
        --bg-deep: #000000;
        --radius-lg: 20px;
        --radius-md: 14px;
        --radius-sm: 8px;

        --transition-snappy: all 0.2s cubic-bezier(0.25, 0.8, 0.25, 1);
        --transition-smooth: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }

    @media (prefers-reduced-transparency: reduce) {
        :root {
            --glass-surface: rgba(30, 30, 30, 0.95);
            --glass-blur: 0px;
            --glass-hover: rgba(50, 50, 50, 1);
        }
    }

    @media (prefers-reduced-motion: reduce) {
        :root {
            --transition-snappy: none;
            --transition-smooth: none;
        }
        * {
            animation: none !important;
            transition: none !important;
        }
    }"""
root_replace = """    :root {
        --glass-surface: rgba(30, 30, 35, 0.3);
        --glass-border: rgba(255, 255, 255, 0.08);
        --glass-border-strong: rgba(255, 255, 255, 0.15);
        --glass-highlight: inset 0 1px 0 0 rgba(255, 255, 255, 0.15), inset 0 0 20px rgba(255, 255, 255, 0.02);
        --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6), 0 2px 8px 0 rgba(0, 0, 0, 0.3);
        --glass-active: rgba(255, 255, 255, 0.05);
        --glass-hover: rgba(60, 60, 65, 0.45);
        --glass-blur: blur(35px) saturate(180%);
        --accent-orange: #fa9400;
        --accent-glow: rgba(250, 148, 0, 0.6);
        --text-primary: #f5f5f7;
        --text-secondary: #a1a1a6;
        --bg-deep: #050505;
        --radius-lg: 24px;
        --radius-md: 16px;
        --radius-sm: 10px;

        /* Apple-like spring curves */
        --transition-snappy: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        --transition-smooth: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
    }

    @media (prefers-reduced-transparency: reduce) {
        :root {
            --glass-surface: rgba(35, 35, 40, 0.95);
            --glass-blur: none;
            --glass-hover: rgba(55, 55, 60, 1);
        }
    }

    @media (prefers-reduced-motion: reduce) {
        :root {
            --transition-snappy: none;
            --transition-smooth: none;
        }
        * {
            animation: none !important;
            transition: none !important;
        }
    }"""
content = content.replace(root_search, root_replace)

# 2. Update Body Background to allow refraction
body_search = """    body {
        background-color: var(--bg-deep);
        background-image: radial-gradient(circle at 50% 0%, #1a1a1a 0%, #000000 100%);
        color: var(--text-primary);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 13px;
        margin: 0;
        padding: 0;
        -webkit-font-smoothing: antialiased;
    }"""
body_replace = """    body {
        background-color: var(--bg-deep);
        /* Deep cinematic mesh gradient for glass to refract */
        background-image:
            radial-gradient(circle at 15% 50%, rgba(250, 148, 0, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 85% 30%, rgba(41, 182, 246, 0.05) 0%, transparent 40%),
            radial-gradient(circle at 50% -20%, rgba(255, 255, 255, 0.05) 0%, transparent 60%);
        background-attachment: fixed;
        color: var(--text-primary);
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 13px;
        margin: 0;
        padding: 0;
        -webkit-font-smoothing: antialiased;
    }"""
content = content.replace(body_search, body_replace)

with open('index_v019_Board_right_click_Fixed.html', 'w', encoding='utf-8') as f:
    f.write(content)
