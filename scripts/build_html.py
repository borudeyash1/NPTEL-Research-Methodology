# -*- coding: utf-8 -*-
import json
import os

with open(r'd:\Interview\SAA\NPTEL\quiz_data\nptel_all_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open(r'd:\Interview\SAA\NPTEL\quiz_data\weekly_assignments.json', 'r', encoding='utf-8') as f:
    weekly_assignments = json.load(f)

with open(r'd:\Interview\SAA\NPTEL\scripts\modules_meta.json', 'r', encoding='utf-8') as f:
    modules_meta = json.load(f)

# HTML Template
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NPTEL Research Methodology - Master Certification Exam & Practice Assessment</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --tcs-blue: #3276b1;
            --tcs-dark-blue: #245580;
            --tcs-light-blue: #e8f1f8;
            --tcs-nav-bg: #3b3f48;
            --tcs-header-gray: #4a5160;
            --tcs-gray-bg: #f4f6f9;
            --tcs-border: #d0d7de;
            --tcs-active-tab: #0077c5;
            
            --answered-green: #5cb85c;
            --not-answered-red: #d9534f;
            --not-visited-gray: #e6e9ed;
            --marked-review-purple: #843b62;
            --marked-answered-purple: #613659;
            
            --text-dark: #222222;
            --text-muted: #555555;
            --text-light: #ffffff;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Segoe UI', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--tcs-gray-bg);
            color: var(--text-dark);
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            font-size: 14px;
        }}

        /* TOP BANNER HEADER */
        .top-banner {{
            background: linear-gradient(90deg, #1f2532 0%, #2e384d 100%);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 6px 16px;
            font-size: 13px;
            border-bottom: 2px solid #005a9e;
            user-select: none;
            height: 44px;
        }}

        .brand-left {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .nptel-badge {{
            background: #ff7700;
            color: #ffffff;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 3px;
            letter-spacing: 0.5px;
            font-size: 12px;
        }}

        .exam-title {{
            font-weight: 600;
            font-size: 14px;
            letter-spacing: 0.3px;
        }}

        .banner-links {{
            display: flex;
            align-items: center;
            gap: 16px;
            font-size: 12px;
        }}

        .banner-link {{
            color: #d8e3ec;
            text-decoration: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 5px;
        }}

        .banner-link:hover {{
            color: #ffffff;
            text-decoration: underline;
        }}

        /* SUB-HEADER / CONTROLS STRIP */
        .sub-header-strip {{
            background: #ffffff;
            border-bottom: 1px solid var(--tcs-border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 6px 16px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            height: 48px;
        }}

        .filter-controls {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .custom-select {{
            padding: 4px 10px;
            border: 1px solid #b8c4d0;
            border-radius: 4px;
            font-size: 13px;
            font-family: inherit;
            background: #ffffff;
            color: #2c3e50;
            outline: none;
            max-width: 380px;
        }}

        .custom-select:focus {{
            border-color: #0077c5;
            box-shadow: 0 0 0 2px rgba(0, 119, 197, 0.2);
        }}

        .mode-toggle-group {{
            display: flex;
            align-items: center;
            background: #ebf1f6;
            padding: 2px;
            border-radius: 4px;
            border: 1px solid #cbd6e2;
        }}

        .mode-btn {{
            border: none;
            background: transparent;
            padding: 4px 12px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            border-radius: 3px;
            color: #486581;
            transition: all 0.2s;
        }}

        .mode-btn.active {{
            background: #0077c5;
            color: #ffffff;
            box-shadow: 0 1px 2px rgba(0,0,0,0.15);
        }}

        .timer-badge {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
            font-weight: 700;
            color: #b71c1c;
            background: #ffebee;
            padding: 4px 12px;
            border-radius: 4px;
            border: 1px solid #ffcdd2;
        }}

        /* MAIN CONTAINER (Left content area + Right question palette) */
        .main-container {{
            display: flex;
            flex: 1;
            overflow: hidden;
            background: #ffffff;
        }}

        /* FULL WIDTH QUESTION AREA */
        .question-viewport {{
            flex: 1;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            border-right: 1px solid var(--tcs-border);
            background: #ffffff;
            position: relative;
        }}

        .question-header-bar {{
            background: #ebf3fa;
            border-bottom: 1px solid #d2e2f0;
            padding: 8px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 13px;
            user-select: none;
        }}

        .q-meta-left {{
            display: flex;
            align-items: center;
            gap: 15px;
            font-weight: 600;
            color: #1f3b58;
        }}

        .q-meta-right {{
            display: flex;
            align-items: center;
            gap: 14px;
            color: #486581;
        }}

        .badge-type {{
            background: #dbeafe;
            color: #1d4ed8;
            font-size: 11px;
            padding: 2px 8px;
            border-radius: 12px;
            border: 1px solid #bfdbfe;
        }}

        .badge-points {{
            background: #e2e8f0;
            color: #334155;
            font-size: 11px;
            padding: 2px 8px;
            border-radius: 12px;
            font-weight: 600;
        }}

        /* FULL WIDTH QUESTION CONTENT */
        .question-body-container {{
            flex: 1;
            padding: 24px 32px;
            overflow-y: auto;
        }}

        .passage-card {{
            background: #fdfdfd;
            border: 1px solid #e2e8f0;
            border-left: 4px solid #0284c7;
            padding: 16px 20px;
            border-radius: 4px;
            margin-bottom: 20px;
            font-size: 13.5px;
            line-height: 1.6;
            color: #334155;
        }}

        .question-title-text {{
            font-size: 16px;
            font-weight: 600;
            line-height: 1.5;
            color: #0f172a;
            margin-bottom: 20px;
        }}

        /* FULL WIDTH OPTIONS (BELOW QUESTION) */
        .options-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-top: 10px;
        }}

        .option-item {{
            display: flex;
            align-items: flex-start;
            gap: 14px;
            background: #ffffff;
            border: 1.5px solid #d8e2ec;
            padding: 12px 18px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.15s ease;
            user-select: none;
            font-size: 14.5px;
            line-height: 1.5;
        }}

        .option-item:hover {{
            background: #f8fafc;
            border-color: #94a3b8;
        }}

        .option-item.selected {{
            background: #eff6ff;
            border-color: #2563eb;
            box-shadow: 0 1px 3px rgba(37, 99, 235, 0.15);
        }}

        .option-item input[type="radio"],
        .option-item input[type="checkbox"] {{
            margin-top: 4px;
            width: 17px;
            height: 17px;
            cursor: pointer;
            accent-color: #0077c5;
        }}

        .option-label-text {{
            flex: 1;
            color: #1e293b;
        }}

        /* PRACTICE FEEDBACK CONTAINER */
        .feedback-container {{
            margin-top: 24px;
            border-radius: 6px;
            padding: 16px 20px;
            display: none;
            animation: fadeIn 0.3s ease;
        }}

        .feedback-correct {{
            background: #f0fdf4;
            border: 1.5px solid #86efac;
            color: #166534;
        }}

        .feedback-incorrect {{
            background: #fef2f2;
            border: 1.5px solid #fca5a5;
            color: #991b1b;
        }}

        .feedback-badge {{
            display: inline-block;
            font-weight: 700;
            font-size: 13px;
            padding: 3px 10px;
            border-radius: 4px;
            margin-bottom: 8px;
        }}

        .feedback-correct .feedback-badge {{
            background: #22c55e;
            color: #ffffff;
        }}

        .feedback-incorrect .feedback-badge {{
            background: #ef4444;
            color: #ffffff;
        }}

        .accepted-answer-box {{
            margin-top: 8px;
            font-weight: 600;
            font-size: 13.5px;
            padding: 8px 12px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 4px;
            border: 1px dashed currentColor;
        }}

        .explanation-text {{
            margin-top: 10px;
            font-size: 13.5px;
            line-height: 1.55;
        }}

        /* BOTTOM ACTION BUTTONS */
        .bottom-action-bar {{
            background: #f8fafc;
            border-top: 1px solid var(--tcs-border);
            padding: 10px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            user-select: none;
            height: 54px;
        }}

        .action-left-btns, .action-right-btns {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .btn-tcs {{
            padding: 7px 18px;
            font-size: 13px;
            font-weight: 600;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.15s ease;
            font-family: inherit;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }}

        .btn-default {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            color: #334155;
        }}

        .btn-default:hover {{
            background: #f1f5f9;
            border-color: #94a3b8;
        }}

        .btn-primary {{
            background: #0077c5;
            border: 1px solid #005a9e;
            color: #ffffff;
        }}

        .btn-primary:hover {{
            background: #005fa3;
        }}

        .btn-mark {{
            background: #6b21a8;
            border: 1px solid #581c87;
            color: #ffffff;
        }}

        .btn-mark:hover {{
            background: #581c87;
        }}

        .btn-submit {{
            background: #10b981;
            border: 1px solid #059669;
            color: #ffffff;
        }}

        .btn-submit:hover {{
            background: #059669;
        }}

        /* RIGHT PALETTE SIDEBAR */
        .palette-sidebar {{
            width: 320px;
            background: #f8fafc;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            user-select: none;
        }}

        .candidate-card {{
            background: #ffffff;
            border-bottom: 1px solid var(--tcs-border);
            padding: 10px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .candidate-avatar {{
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: #0077c5;
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 16px;
            border: 2px solid #b8d9f2;
        }}

        .candidate-info {{
            line-height: 1.3;
        }}

        .candidate-name {{
            font-weight: 700;
            font-size: 13.5px;
            color: #1e293b;
        }}

        .candidate-sub {{
            font-size: 11.5px;
            color: #64748b;
        }}

        /* LEGEND STRIP */
        .legend-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 6px 10px;
            padding: 10px 14px;
            background: #ffffff;
            border-bottom: 1px solid var(--tcs-border);
            font-size: 11px;
            color: #475569;
        }}

        .legend-item {{
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .legend-badge {{
            width: 22px;
            height: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 10.5px;
            border-radius: 3px;
        }}

        /* TCS STATUS BADGE SHAPES */
        .status-answered {{
            background-color: #22c55e !important;
            color: #ffffff !important;
            border-color: #16a34a !important;
            border-radius: 4px;
        }}

        .status-not-answered {{
            background-color: #ef4444 !important;
            color: #ffffff !important;
            border-color: #dc2626 !important;
            border-radius: 4px;
        }}

        .status-not-visited {{
            background-color: #f1f5f9 !important;
            color: #1e293b !important;
            border: 1.5px solid #cbd5e1 !important;
            border-radius: 4px;
        }}

        .status-marked {{
            background-color: #8b5cf6 !important;
            color: #ffffff !important;
            border-color: #7c3aed !important;
            border-radius: 50% !important;
        }}

        .status-marked-answered {{
            background-color: #7c3aed !important;
            color: #ffffff !important;
            border-color: #6d28d9 !important;
            border-radius: 50% !important;
            position: relative;
        }}

        .status-marked-answered::after {{
            content: '';
            position: absolute;
            bottom: 1px;
            right: 1px;
            width: 8px;
            height: 8px;
            background: #22c55e;
            border-radius: 50%;
            border: 1.5px solid #ffffff;
        }}

        /* PALETTE QUESTION GRID */
        .palette-section-header {{
            background: #e2e8f0;
            padding: 6px 14px;
            font-weight: 700;
            font-size: 12px;
            color: #1e293b;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .palette-scroll-box {{
            flex: 1;
            overflow-y: auto;
            padding: 12px;
        }}

        .palette-grid {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 8px;
        }}

        .palette-btn {{
            aspect-ratio: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            border: 1.5px solid #cbd5e1;
            background: #f1f5f9;
            color: #1e293b;
            border-radius: 4px;
            transition: all 0.15s ease;
            position: relative;
            padding: 0;
            box-shadow: 0 1px 2px rgba(0,0,0,0.06);
        }}

        .palette-btn:hover {{
            transform: scale(1.06);
            box-shadow: 0 2px 5px rgba(0,0,0,0.15);
        }}

        .palette-btn.active-q {{
            outline: 2.5px solid #0077c5 !important;
            outline-offset: 2px;
            box-shadow: 0 0 0 2px rgba(0, 119, 197, 0.4);
        }}

        /* RESULTS MODAL */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.75);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 2000;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.25s ease;
        }}

        .modal-overlay.open {{
            opacity: 1;
            pointer-events: auto;
        }}

        .modal-box {{
            background: #ffffff;
            border-radius: 8px;
            width: 90%;
            max-width: 680px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.25);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

        .modal-header {{
            background: #0f172a;
            color: #ffffff;
            padding: 16px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .modal-header h2 {{
            font-size: 17px;
            font-weight: 700;
        }}

        .modal-body {{
            padding: 24px;
            max-height: 70vh;
            overflow-y: auto;
        }}

        .score-hero {{
            text-align: center;
            padding: 16px;
            background: #f8fafc;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
            margin-bottom: 20px;
        }}

        .score-hero-num {{
            font-size: 38px;
            font-weight: 800;
            color: #0077c5;
        }}

        .score-hero-label {{
            font-size: 14px;
            color: #64748b;
            font-weight: 600;
        }}

        .stats-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13.5px;
            margin-bottom: 20px;
        }}

        .stats-table th, .stats-table td {{
            padding: 8px 12px;
            border: 1px solid #e2e8f0;
            text-align: left;
        }}

        .stats-table th {{
            background: #f1f5f9;
            color: #334155;
        }}

        .modal-footer {{
            background: #f8fafc;
            border-top: 1px solid #e2e8f0;
            padding: 12px 20px;
            display: flex;
            justify-content: flex-end;
            gap: 10px;
        }}

        /* EXAM MODE LOCKDOWN STYLES */
        body.exam-lockdown {{
            user-select: none !important;
            -webkit-user-select: none !important;
            -moz-user-select: none !important;
            -ms-user-select: none !important;
        }}

        .security-warning-toast {{
            position: fixed;
            top: 50px;
            left: 50%;
            transform: translateX(-50%);
            background: #b91c1c;
            color: #ffffff;
            padding: 12px 24px;
            border-radius: 6px;
            font-weight: 700;
            font-size: 14px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.35);
            z-index: 99999;
            display: none;
            align-items: center;
            gap: 10px;
            animation: fadeIn 0.2s ease;
            border: 2px solid #fecaca;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translate(-50%, -10px); }}
            to {{ opacity: 1; transform: translate(-50%, 0); }}
        }}
    </style>
</head>
<body>

    <!-- EXAM SECURITY / PROCTORING WARNING TOAST -->
    <div id="securityWarningToast" class="security-warning-toast">
        ⚠️ <span id="securityWarningMsg">Action not allowed in Exam Mode!</span>
    </div>

    <!-- TOP TCS iON NAV BAR -->
    <header class="top-banner">
        <div class="brand-left">
            <span class="nptel-badge">NPTEL</span>
            <span class="exam-title">Research Methodology Master Certification Assessment (51 Modules • 510 Questions)</span>
        </div>
        <div class="banner-links">
            <span class="banner-link" onclick="toggleInstructions()">ℹ Question Paper</span>
            <span class="banner-link" onclick="toggleInstructions()">ℹ View Instructions</span>
            <span class="banner-link" onclick="resetActiveModule()">🔄 Reset Module</span>
            <button class="btn-tcs btn-submit" style="padding: 4px 14px; font-size: 12px; margin-left: 8px; font-weight: 700; box-shadow: 0 1px 3px rgba(0,0,0,0.3);" onclick="submitAssessment()">Submit Exam</button>
        </div>
    </header>

    <!-- SUB CONTROLS & FILTER STRIP -->
    <div class="sub-header-strip">
        <div class="filter-controls">
            <label style="font-weight: 600; font-size: 12.5px; color: #475569;">Select Module:</label>
            <select id="moduleSelect" class="custom-select" onchange="onModuleChange(this.value)">
                <option value="all">All 51 Modules (510 Questions Comprehensive Exam)</option>
            </select>

            <div class="mode-toggle-group">
                <button id="practiceModeBtn" class="mode-btn active" onclick="setMode('practice')">Practice Mode</button>
                <button id="examModeBtn" class="mode-btn" onclick="setMode('exam')">Exam Mode</button>
            </div>
        </div>

        <div style="display: flex; align-items: center; gap: 12px;">
            <div id="timerContainer" class="timer-badge" style="display: none;">
                ⏱ <span id="timerDisplay">180:00</span>
            </div>
            <div style="font-size: 12px; color: #64748b; font-weight: 600;">
                Language: <b>English</b>
            </div>
        </div>
    </div>

    <!-- MAIN TWO COLUMN WORKSPACE -->
    <main class="main-container">
        
        <!-- FULL WIDTH QUESTION AREA -->
        <section class="question-viewport">
            
            <!-- Question metadata bar -->
            <div class="question-header-bar">
                <div class="q-meta-left">
                    <span id="currentQuestionNum">Question No. 1</span>
                    <span id="currentWeekModule" style="color: #0284c7; font-weight: 600;">Module 1 (Week 1)</span>
                </div>
                <div class="q-meta-right">
                    <span id="qTypeBadge" class="badge-type">Multiple Choice Question</span>
                    <span class="badge-points">1 Point | Negative: 0</span>
                </div>
            </div>

            <!-- Scrollable Question & Options Body -->
            <div class="question-body-container">
                <div id="passageContainer" class="passage-card" style="display: none;"></div>
                
                <div id="questionTitle" class="question-title-text">
                    Loading question text...
                </div>

                <!-- OPTIONS LIST -->
                <div id="optionsList" class="options-list"></div>

                <!-- PRACTICE MODE INSTANT FEEDBACK -->
                <div id="practiceFeedback" class="feedback-container">
                    <div id="feedbackBadge" class="feedback-badge">Yes, the answer is correct!</div>
                    <div id="acceptedAnswerBox" class="accepted-answer-box"></div>
                    <div id="explanationBox" class="explanation-text"></div>
                </div>
            </div>

            <!-- BOTTOM CONTROLS STRIP -->
            <div class="bottom-action-bar">
                <div class="action-left-btns">
                    <button class="btn-tcs btn-mark" onclick="markForReviewAndNext()">Mark for Review & Next</button>
                    <button class="btn-tcs btn-default" onclick="clearCurrentResponse()">Clear Response</button>
                    <button id="checkAnswerBtn" class="btn-tcs btn-default" onclick="checkCurrentAnswer()">Check Answer</button>
                </div>
                <div class="action-right-btns">
                    <button class="btn-tcs btn-default" onclick="prevQuestion()">Previous</button>
                    <button class="btn-tcs btn-primary" onclick="saveAndNext()">Save & Next</button>
                </div>
            </div>

        </section>

        <!-- RIGHT PALETTE SIDEBAR -->
        <aside class="palette-sidebar">
            
            <!-- Candidate profile -->
            <div class="candidate-card">
                <div class="candidate-avatar">RM</div>
                <div class="candidate-info">
                    <div class="candidate-name">Research Scholar</div>
                    <div class="candidate-sub">NPTEL IIT Madras Candidate</div>
                </div>
            </div>

            <!-- Legend stats -->
            <div class="legend-grid">
                <div class="legend-item">
                    <span class="legend-badge status-answered" id="countAnswered">0</span> Answered
                </div>
                <div class="legend-item">
                    <span class="legend-badge status-not-answered" id="countNotAnswered">0</span> Not Answered
                </div>
                <div class="legend-item">
                    <span class="legend-badge status-not-visited" id="countNotVisited">0</span> Not Visited
                </div>
                <div class="legend-item">
                    <span class="legend-badge status-marked" id="countMarked">0</span> Marked for Review
                </div>
                <div class="legend-item" style="grid-column: span 2;">
                    <span class="legend-badge status-marked-answered" id="countMarkedAnswered">0</span> Answered & Marked for Review
                </div>
            </div>

            <!-- Section title -->
            <div class="palette-section-header">
                <span id="paletteTitle">Questions Palette</span>
                <span id="paletteFilterCount" style="color: #64748b; font-size: 11px;">10 Questions</span>
            </div>

            <!-- Question Numbers Grid -->
            <div class="palette-scroll-box">
                <div id="paletteGrid" class="palette-grid"></div>
            </div>

        </aside>

    </main>

    <!-- ASSESSMENT RESULTS MODAL -->
    <div id="resultsModal" class="modal-overlay">
        <div class="modal-box">
            <div class="modal-header">
                <h2>Assessment Performance Summary</h2>
                <button style="background: none; border: none; color: white; font-size: 18px; cursor: pointer;" onclick="closeModal()">✕</button>
            </div>
            <div class="modal-body">
                <div class="score-hero">
                    <div id="modalScoreDisplay" class="score-hero-num">85%</div>
                    <div id="modalScoreLabel" class="score-hero-label">Total Score: 85 / 100 Points</div>
                </div>

                <table class="stats-table">
                    <tr><th>Metric</th><th>Count / Percentage</th></tr>
                    <tr><td>Total Questions Attempted</td><td id="statAttempted">0</td></tr>
                    <tr><td>Correct Answers</td><td id="statCorrect" style="color: #16a34a; font-weight: 700;">0</td></tr>
                    <tr><td>Incorrect Answers</td><td id="statIncorrect" style="color: #dc2626; font-weight: 700;">0</td></tr>
                    <tr><td>Unattempted Questions</td><td id="statUnattempted">0</td></tr>
                    <tr><td>Marked for Review</td><td id="statMarked">0</td></tr>
                </table>
            </div>
            <div class="modal-footer">
                <button class="btn-tcs btn-default" onclick="closeModal()">Review Questions</button>
                <button class="btn-tcs btn-primary" onclick="restartAssessment()">Restart Assessment</button>
            </div>
        </div>
    </div>

    <script>
        // MASTER QUESTIONS DATA
        const rawQuestions = {json.dumps(questions)};
        const weeklyQuestions = {json.dumps(weekly_assignments)};
        const modulesMeta = {json.dumps(modules_meta)};

        // STATE
        let currentMode = 'practice'; // 'practice' or 'exam'
        let selectedModule = 'all';
        let activeQuestions = [...rawQuestions];
        let currentIndex = 0;
        
        // user state per question id
        // status: 'not-visited', 'not-answered', 'answered', 'marked', 'marked-answered'
        let userResponses = {{}};
        let timerInterval = null;
        let timeRemainingSeconds = 180 * 60; // 3 hours for exam mode

        // INITIALIZATION
        window.addEventListener('DOMContentLoaded', () => {{
            populateModuleDropdown();
            initQuestionState();
            renderQuestion(0);
            updatePalette();
            updateStatsCounts();
        }});

        function populateModuleDropdown() {{
            const select = document.getElementById('moduleSelect');
            select.innerHTML = '';

            // 1. All questions option
            const allOpt = document.createElement('option');
            allOpt.value = 'all';
            allOpt.textContent = '📚 Comprehensive Exam - All 51 Lecture Modules (510 Questions)';
            select.appendChild(allOpt);

            // 2. All 12 Weekly Tests combined
            const allWeeklyOpt = document.createElement('option');
            allWeeklyOpt.value = 'weekly_all';
            allWeeklyOpt.textContent = '🎯 All 12 Official Weekly Tests Combined (120 Questions)';
            select.appendChild(allWeeklyOpt);

            // 3. Optgroup for 12 Weekly Assignment Tests
            const weeklyGroup = document.createElement('optgroup');
            weeklyGroup.label = '📝 OFFICIAL NPTEL WEEKLY ASSIGNMENTS (WEEKS 1 - 12)';
            for (let w = 1; w <= 12; w++) {{
                const opt = document.createElement('option');
                opt.value = `week_${{w}}`;
                opt.textContent = `Week ${{w}} Assignment Test (10 Questions)`;
                weeklyGroup.appendChild(opt);
            }}
            select.appendChild(weeklyGroup);

            // 4. Optgroup for 51 Course Lecture Modules
            const lectureGroup = document.createElement('optgroup');
            lectureGroup.label = '📖 COURSE LECTURE MODULES (1 - 51)';
            modulesMeta.forEach(m => {{
                const opt = document.createElement('option');
                opt.value = String(m[0]);
                opt.textContent = `Module ${{m[0]}}: ${{m[1]}} (Week ${{m[2]}})`;
                lectureGroup.appendChild(opt);
            }});
            select.appendChild(lectureGroup);
        }}

        function initQuestionState() {{
            userResponses = {{}};
            // Initialize for both raw lecture questions and weekly test questions
            rawQuestions.forEach(q => {{
                userResponses[q.id] = {{
                    selected: q.type === 'multi' ? [] : null,
                    status: 'not-visited',
                    checkedInPractice: false
                }};
            }});
            weeklyQuestions.forEach(q => {{
                userResponses[q.id] = {{
                    selected: q.type === 'multi' ? [] : null,
                    status: 'not-visited',
                    checkedInPractice: false
                }};
            }});
        }}

        function onModuleChange(modVal) {{
            selectedModule = modVal;
            if (modVal === 'all') {{
                activeQuestions = [...rawQuestions];
            }} else if (modVal === 'weekly_all') {{
                activeQuestions = [...weeklyQuestions];
            }} else if (modVal.startsWith('week_')) {{
                const wNum = parseInt(modVal.replace('week_', ''));
                activeQuestions = weeklyQuestions.filter(q => q.week === wNum);
            }} else {{
                const mNum = parseInt(modVal);
                activeQuestions = rawQuestions.filter(q => q.module === mNum);
            }}
            currentIndex = 0;
            document.getElementById('paletteFilterCount').textContent = `${{activeQuestions.length}} Questions`;
            renderQuestion(0);
            updatePalette();
            updateStatsCounts();
        }}

        function setMode(mode) {{
            currentMode = mode;
            document.getElementById('practiceModeBtn').classList.toggle('active', mode === 'practice');
            document.getElementById('examModeBtn').classList.toggle('active', mode === 'exam');
            
            const timer = document.getElementById('timerContainer');
            const checkBtn = document.getElementById('checkAnswerBtn');

            if (mode === 'exam') {{
                timer.style.display = 'flex';
                checkBtn.style.display = 'none';
                document.body.classList.add('exam-lockdown');
                enterFullScreen();
                enableExamSecurity();
                startExamTimer();
                showSecurityToast('Exam Mode Activated: Fullscreen enforced. Copy/Paste, Screenshots, and Tab Switching are strictly prohibited.');
            }} else {{
                timer.style.display = 'none';
                checkBtn.style.display = 'inline-flex';
                document.body.classList.remove('exam-lockdown');
                disableExamSecurity();
                clearInterval(timerInterval);
                exitFullScreen();
            }}
            renderQuestion(currentIndex);
        }}

        function enterFullScreen() {{
            const el = document.documentElement;
            if (el.requestFullscreen) {{
                el.requestFullscreen().catch(err => console.log('Fullscreen request ignored or denied'));
            }} else if (el.webkitRequestFullscreen) {{
                el.webkitRequestFullscreen();
            }} else if (el.msRequestFullscreen) {{
                el.msRequestFullscreen();
            }}
        }}

        function exitFullScreen() {{
            if (document.fullscreenElement) {{
                if (document.exitFullscreen) {{
                    document.exitFullscreen().catch(err => console.log('Exit fullscreen error'));
                }} else if (document.webkitExitFullscreen) {{
                    document.webkitExitFullscreen();
                }}
            }}
        }}

        let toastTimeout = null;
        function showSecurityToast(msg) {{
            const toast = document.getElementById('securityWarningToast');
            const textSpan = document.getElementById('securityWarningMsg');
            textSpan.textContent = msg;
            toast.style.display = 'flex';
            if (toastTimeout) clearTimeout(toastTimeout);
            toastTimeout = setTimeout(() => {{
                toast.style.display = 'none';
            }}, 4000);
        }}

        // EXAM SECURITY EVENT HANDLERS
        function handleCopyCutPaste(e) {{
            if (currentMode === 'exam') {{
                e.preventDefault();
                showSecurityToast('Security Warning: Copying, cutting, and pasting are strictly disabled during Exam Mode!');
                return false;
            }}
        }}

        function handleContextMenu(e) {{
            if (currentMode === 'exam') {{
                e.preventDefault();
                showSecurityToast('Security Warning: Right-click context menu is disabled during Exam Mode!');
                return false;
            }}
        }}

        function handleKeyDown(e) {{
            if (currentMode !== 'exam') return;

            // Block PrintScreen
            if (e.key === 'PrintScreen' || e.code === 'PrintScreen' || e.keyCode === 44) {{
                e.preventDefault();
                showSecurityToast('Security Alert: Screenshots are strictly prohibited during the assessment!');
                if (navigator.clipboard && navigator.clipboard.writeText) {{
                    navigator.clipboard.writeText('');
                }}
                return false;
            }}

            // Block F12, Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+U (Inspect / DevTools)
            if (e.keyCode === 123 || 
                (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'J' || e.key === 'j' || e.key === 'C' || e.key === 'c')) ||
                (e.ctrlKey && (e.key === 'u' || e.key === 'U'))) {{
                e.preventDefault();
                showSecurityToast('Security Alert: Developer inspection tools are disabled in Exam Mode!');
                return false;
            }}

            // Block Refresh keys (F5, Ctrl+R, Ctrl+F5)
            if (e.keyCode === 116 || (e.ctrlKey && (e.key === 'r' || e.key === 'R'))) {{
                e.preventDefault();
                showSecurityToast('Security Alert: Refreshing during the exam is prohibited! Your responses may be lost.');
                return false;
            }}

            // Block Copy / Cut / Paste shortcuts (Ctrl+C, Ctrl+V, Ctrl+X, Ctrl+A)
            if (e.ctrlKey && ['c', 'v', 'x', 'a', 'p', 's'].includes(e.key.toLowerCase())) {{
                e.preventDefault();
                showSecurityToast('Security Alert: Keyboard shortcut blocked in Exam Mode!');
                return false;
            }}
        }}

        function handleBeforeUnload(e) {{
            if (currentMode === 'exam') {{
                const warningMsg = 'Exam in Progress! If you leave or refresh this page, your ongoing exam progress may be discarded.';
                e.preventDefault();
                e.returnValue = warningMsg;
                return warningMsg;
            }}
        }}

        function handleVisibilityChange() {{
            if (currentMode === 'exam' && document.hidden) {{
                showSecurityToast('Proctoring Warning: Tab or window switching detected! Please return to the exam viewport immediately.');
            }}
        }}

        function handleFullscreenChange() {{
            if (currentMode === 'exam' && !document.fullscreenElement) {{
                showSecurityToast('Warning: You have exited fullscreen! Please stay in fullscreen mode during the examination.');
            }}
        }}

        let securityBound = false;
        function enableExamSecurity() {{
            if (securityBound) return;
            document.addEventListener('copy', handleCopyCutPaste, true);
            document.addEventListener('cut', handleCopyCutPaste, true);
            document.addEventListener('paste', handleCopyCutPaste, true);
            document.addEventListener('contextmenu', handleContextMenu, true);
            window.addEventListener('keydown', handleKeyDown, true);
            window.addEventListener('beforeunload', handleBeforeUnload);
            document.addEventListener('visibilitychange', handleVisibilityChange);
            document.addEventListener('fullscreenchange', handleFullscreenChange);
            securityBound = true;
        }}

        function disableExamSecurity() {{
            if (!securityBound) return;
            document.removeEventListener('copy', handleCopyCutPaste, true);
            document.removeEventListener('cut', handleCopyCutPaste, true);
            document.removeEventListener('paste', handleCopyCutPaste, true);
            document.removeEventListener('contextmenu', handleContextMenu, true);
            window.removeEventListener('keydown', handleKeyDown, true);
            window.removeEventListener('beforeunload', handleBeforeUnload);
            document.removeEventListener('visibilitychange', handleVisibilityChange);
            document.removeEventListener('fullscreenchange', handleFullscreenChange);
            securityBound = false;
        }}

        function startExamTimer() {{
            clearInterval(timerInterval);
            timeRemainingSeconds = Math.min(180 * 60, activeQuestions.length * 120);
            updateTimerDisplay();
            timerInterval = setInterval(() => {{
                timeRemainingSeconds--;
                updateTimerDisplay();
                if (timeRemainingSeconds <= 0) {{
                    clearInterval(timerInterval);
                    alert('Time limit reached! Submitting your exam automatically.');
                    submitAssessment();
                }}
            }}, 1000);
        }}

        function updateTimerDisplay() {{
            const mins = Math.floor(timeRemainingSeconds / 60);
            const secs = timeRemainingSeconds % 60;
            document.getElementById('timerDisplay').textContent = 
                `${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}`;
        }}

        function renderQuestion(idx) {{
            if (idx < 0 || idx >= activeQuestions.length) return;
            currentIndex = idx;
            const q = activeQuestions[idx];
            const state = userResponses[q.id];

            // Mark visited if not yet touched
            if (state.status === 'not-visited') {{
                state.status = 'not-answered';
            }}

            document.getElementById('currentQuestionNum').textContent = `Question No. ${{idx + 1}} of ${{activeQuestions.length}}`;
            const modLabel = q.moduleTitle ? q.moduleTitle : `Weekly Assignment Test - Week ${{q.week}}`;
            document.getElementById('currentWeekModule').textContent = modLabel;
            document.getElementById('qTypeBadge').textContent = q.type === 'multi' ? 'Multiple Choice (Select all correct)' : 'Multiple Choice Question';

            // Passage
            const passBox = document.getElementById('passageContainer');
            if (q.passage) {{
                passBox.style.display = 'block';
                passBox.innerHTML = `<b>Read the passage below and answer the question:</b><br><br>${{q.passage}}`;
            }} else {{
                passBox.style.display = 'none';
            }}

            // Question title
            document.getElementById('questionTitle').textContent = q.question;

            // Render options
            const optContainer = document.getElementById('optionsList');
            optContainer.innerHTML = '';

            const isMulti = q.type === 'multi';

            q.options.forEach((optText, oIdx) => {{
                const item = document.createElement('label');
                item.className = 'option-item';
                
                const isSelected = isMulti 
                    ? state.selected.includes(oIdx) 
                    : state.selected === oIdx;

                if (isSelected) item.classList.add('selected');

                const input = document.createElement('input');
                input.type = isMulti ? 'checkbox' : 'radio';
                input.name = `question_option_${{q.id}}`;
                input.checked = isSelected;
                
                input.onchange = () => handleOptionSelection(q.id, oIdx, isMulti);

                const span = document.createElement('span');
                span.className = 'option-label-text';
                span.textContent = optText;

                item.appendChild(input);
                item.appendChild(span);
                optContainer.appendChild(item);
            }});

            // Feedback box for practice mode
            const fbBox = document.getElementById('practiceFeedback');
            if (currentMode === 'practice' && state.checkedInPractice) {{
                showPracticeFeedback(q, state);
            }} else {{
                fbBox.style.display = 'none';
            }}

            updatePalette();
            updateStatsCounts();
        }}

        function handleOptionSelection(qId, oIdx, isMulti) {{
            const state = userResponses[qId];
            if (isMulti) {{
                if (state.selected.includes(oIdx)) {{
                    state.selected = state.selected.filter(x => x !== oIdx);
                }} else {{
                    state.selected.push(oIdx);
                }}
            }} else {{
                state.selected = oIdx;
            }}

            const hasAns = isMulti ? state.selected.length > 0 : state.selected !== null;
            if (hasAns) {{
                if (state.status === 'marked' || state.status === 'marked-answered') {{
                    state.status = 'marked-answered';
                }} else {{
                    state.status = 'answered';
                }}
            }} else {{
                state.status = 'not-answered';
            }}

            state.checkedInPractice = false;
            renderQuestion(currentIndex);
        }}

        function checkCurrentAnswer() {{
            const q = activeQuestions[currentIndex];
            const state = userResponses[q.id];
            state.checkedInPractice = true;
            showPracticeFeedback(q, state);
        }}

        function showPracticeFeedback(q, state) {{
            const fbBox = document.getElementById('practiceFeedback');
            const badge = document.getElementById('feedbackBadge');
            const accBox = document.getElementById('acceptedAnswerBox');
            const expBox = document.getElementById('explanationBox');

            const isMulti = q.type === 'multi';
            let isCorrect = false;

            if (isMulti) {{
                const userArr = [...state.selected].sort();
                const ansArr = [...q.answer].sort();
                isCorrect = JSON.stringify(userArr) === JSON.stringify(ansArr);
            }} else {{
                isCorrect = state.selected === q.answer;
            }}

            fbBox.style.display = 'block';
            if (isCorrect) {{
                fbBox.className = 'feedback-container feedback-correct';
                badge.textContent = '✔ Yes, the answer is correct! Score: 1';
            }} else {{
                fbBox.className = 'feedback-container feedback-incorrect';
                badge.textContent = '✖ Incorrect Response';
            }}

            // Accepted text
            const acceptedAnswersText = isMulti 
                ? q.answer.map(idx => q.options[idx]).join(', ')
                : q.options[q.answer];

            accBox.textContent = `Accepted Answer: ${{acceptedAnswersText}}`;
            expBox.innerHTML = `<b>NPTEL Concept Explanation:</b> ${{q.explanation}}`;
        }}

        function saveAndNext() {{
            const q = activeQuestions[currentIndex];
            const state = userResponses[q.id];
            const hasAns = q.type === 'multi' ? state.selected.length > 0 : state.selected !== null;
            
            if (hasAns) {{
                state.status = 'answered';
            }} else {{
                state.status = 'not-answered';
            }}

            if (currentIndex < activeQuestions.length - 1) {{
                renderQuestion(currentIndex + 1);
            }} else {{
                alert('You have reached the end of the question set.');
            }}
        }}

        function markForReviewAndNext() {{
            const q = activeQuestions[currentIndex];
            const state = userResponses[q.id];
            const hasAns = q.type === 'multi' ? state.selected.length > 0 : state.selected !== null;

            if (hasAns) {{
                state.status = 'marked-answered';
            }} else {{
                state.status = 'marked';
            }}

            if (currentIndex < activeQuestions.length - 1) {{
                renderQuestion(currentIndex + 1);
            }}
        }}

        function clearCurrentResponse() {{
            const q = activeQuestions[currentIndex];
            const state = userResponses[q.id];
            state.selected = q.type === 'multi' ? [] : null;
            state.status = 'not-answered';
            state.checkedInPractice = false;
            renderQuestion(currentIndex);
        }}

        function prevQuestion() {{
            if (currentIndex > 0) {{
                renderQuestion(currentIndex - 1);
            }}
        }}

        function updatePalette() {{
            const grid = document.getElementById('paletteGrid');
            grid.innerHTML = '';

            activeQuestions.forEach((q, idx) => {{
                const state = userResponses[q.id];
                const btn = document.createElement('button');
                btn.className = `palette-btn status-${{state.status}}`;
                if (idx === currentIndex) {{
                    btn.classList.add('active-q');
                }}
                btn.textContent = idx + 1;
                btn.onclick = () => renderQuestion(idx);
                grid.appendChild(btn);
            }});
        }}

        function updateStatsCounts() {{
            let answered = 0, notAnswered = 0, notVisited = 0, marked = 0, markedAnswered = 0;

            activeQuestions.forEach(q => {{
                const st = userResponses[q.id].status;
                if (st === 'answered') answered++;
                else if (st === 'not-answered') notAnswered++;
                else if (st === 'not-visited') notVisited++;
                else if (st === 'marked') marked++;
                else if (st === 'marked-answered') markedAnswered++;
            }});

            document.getElementById('countAnswered').textContent = answered;
            document.getElementById('countNotAnswered').textContent = notAnswered;
            document.getElementById('countNotVisited').textContent = notVisited;
            document.getElementById('countMarked').textContent = marked;
            document.getElementById('countMarkedAnswered').textContent = markedAnswered;
        }}

        function submitAssessment() {{
            let correct = 0, incorrect = 0, unattempted = 0, markedCount = 0;

            activeQuestions.forEach(q => {{
                const state = userResponses[q.id];
                const isMulti = q.type === 'multi';
                const hasAnswer = isMulti ? state.selected.length > 0 : state.selected !== null;

                if (state.status === 'marked' || state.status === 'marked-answered') markedCount++;

                if (!hasAnswer) {{
                    unattempted++;
                }} else {{
                    let isRight = false;
                    if (isMulti) {{
                        const userArr = [...state.selected].sort();
                        const ansArr = [...q.answer].sort();
                        isRight = JSON.stringify(userArr) === JSON.stringify(ansArr);
                    }} else {{
                        isRight = state.selected === q.answer;
                    }}

                    if (isRight) correct++;
                    else incorrect++;
                }}
            }});

            const totalQ = activeQuestions.length;
            const scorePct = Math.round((correct / totalQ) * 100);

            document.getElementById('modalScoreDisplay').textContent = `${{scorePct}}%`;
            document.getElementById('modalScoreLabel').textContent = `Total Score: ${{correct}} / ${{totalQ}} Points`;
            document.getElementById('statAttempted').textContent = totalQ - unattempted;
            document.getElementById('statCorrect').textContent = correct;
            document.getElementById('statIncorrect').textContent = incorrect;
            document.getElementById('statUnattempted').textContent = unattempted;
            document.getElementById('statMarked').textContent = markedCount;

            document.getElementById('resultsModal').classList.add('open');
        }}

        function closeModal() {{
            document.getElementById('resultsModal').classList.remove('open');
        }}

        function restartAssessment() {{
            closeModal();
            initQuestionState();
            renderQuestion(0);
        }}

        function resetActiveModule() {{
            if (confirm('Reset all answers for the current module/exam?')) {{
                initQuestionState();
                renderQuestion(0);
            }}
        }}

        function toggleInstructions() {{
            alert(`NPTEL Examination Guidelines:\n\n1. All 51 Modules of Research Methodology are covered.\n2. In Practice Mode, click "Check Answer" to immediately see the accepted answer, score, and in-depth explanation.\n3. In Exam Mode, time tracking is enabled and answers are validated upon submitting the exam.\n4. Use the full screen question and options layout for comfortable reading.`);
        }}
    </script>
</body>
</html>
"""

out_html = r'd:\Interview\SAA\NPTEL\NPTEL Research Methodology Quiz.html'
with open(out_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated standalone NPTEL Quiz HTML: {out_html}")
print(f"File size: {os.path.getsize(out_html)} bytes")
