def recommend_plan(hours):
    if hours >= 4:
        return "Use Pomodoro (25 mins study, 5 mins break) — 4 sessions."
    elif 2 <= hours < 4:
        return "Focus on flashcards + one quiz review."
    else:
        return "Quick summary review + one mini quiz."