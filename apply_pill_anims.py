with open('index_v019_Board_right_click_Fixed.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure pool-btn scale transitions smoothly
search_pool = """    .pool-btn:active { transform: scale(0.98); }"""
replace_pool = """    .pool-btn:active { transform: scale(0.95); transition: transform 0.1s cubic-bezier(0.34, 1.56, 0.64, 1); }
    .pool-btn {
        transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), background-color 0.2s, color 0.2s;
        transform-origin: center center;
    }"""
content = content.replace(search_pool, replace_pool)

# Add liquid reveal class to react components
search_list_view = """                                                viewMode === 'list' ? ( """
replace_list_view = """                                                viewMode === 'list' ? (
                                                    <div className="w-full animate-liquid-reveal">"""
content = content.replace(search_list_view, replace_list_view)

search_list_view_end = """                                                    </table>
                                                ) : ( """
replace_list_view_end = """                                                    </table>
                                                    </div>
                                                ) : ( """
content = content.replace(search_list_view_end, replace_list_view_end)

search_board_grid = """                                                    <div className="board-grid-container custom-scrollbar"> """
replace_board_grid = """                                                    <div className="board-grid-container custom-scrollbar animate-liquid-reveal"> """
content = content.replace(search_board_grid, replace_board_grid)

with open('index_v019_Board_right_click_Fixed.html', 'w', encoding='utf-8') as f:
    f.write(content)
