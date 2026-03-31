with open('index_v019_Board_right_click_Fixed.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add liquid reveal to main tab content wrappers
search_dash = """                        {/* --- TAB 1: DASHBOARD --- */}
                        {activeTab === "Dashboard" && ( """
replace_dash = """                        {/* --- TAB 1: DASHBOARD --- */}
                        {activeTab === "Dashboard" && (
                            <div className="flex flex-col h-full animate-liquid-reveal"> """
content = content.replace(search_dash, replace_dash)

search_dash_end = """                            </>
                        )} """
replace_dash_end = """                            </div>
                        )} """
content = content.replace(search_dash_end, replace_dash_end)

# Also apply it to Project Overview
search_po = """                        {/* --- TAB 2: PROJECT OVERVIEW --- */}
                        {activeTab === "Project Overview" && (
                            <ProjectOverview shots={shots} projectName={activeProject} initialPool={activePool} />
                        )}"""
replace_po = """                        {/* --- TAB 2: PROJECT OVERVIEW --- */}
                        {activeTab === "Project Overview" && (
                            <div className="h-full animate-liquid-reveal"><ProjectOverview shots={shots} projectName={activeProject} initialPool={activePool} /></div>
                        )}"""
content = content.replace(search_po, replace_po)

# And Artist Breakdown
search_ab = """                        {activeTab === "Artist Breakdown" && (
                            <div className="p-6 h-full flex flex-col gap-6 overflow-hidden animate-fadeIn"> """
replace_ab = """                        {activeTab === "Artist Breakdown" && (
                            <div className="p-6 h-full flex flex-col gap-6 overflow-hidden animate-liquid-reveal"> """
content = content.replace(search_ab, replace_ab)

# And Shot Distribution
search_sd = """                        {activeTab === "Shot Distribution" && (
                            <div className="p-6 h-full flex flex-col gap-6 overflow-hidden animate-fadeIn"> """
replace_sd = """                        {activeTab === "Shot Distribution" && (
                            <div className="p-6 h-full flex flex-col gap-6 overflow-hidden animate-liquid-reveal"> """
content = content.replace(search_sd, replace_sd)

# And Comp Summary
search_cs = """                        {activeTab === "Comp Summary" && (
                            <div className="p-6 h-full flex flex-col gap-8 overflow-y-auto animate-fadeIn custom-scrollbar"> """
replace_cs = """                        {activeTab === "Comp Summary" && (
                            <div className="p-6 h-full flex flex-col gap-8 overflow-y-auto animate-liquid-reveal custom-scrollbar"> """
content = content.replace(search_cs, replace_cs)

# And Roto/Paint Summary
search_rs = """                        {activeTab === "Roto/Paint Summary" && (
                            <div className="p-6 h-full flex flex-col gap-6 overflow-hidden animate-fadeIn"> """
replace_rs = """                        {activeTab === "Roto/Paint Summary" && (
                            <div className="p-6 h-full flex flex-col gap-6 overflow-hidden animate-liquid-reveal"> """
content = content.replace(search_rs, replace_rs)

with open('index_v019_Board_right_click_Fixed.html', 'w', encoding='utf-8') as f:
    f.write(content)
