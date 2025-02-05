-- Create Users Table (Admin & Normal Users)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT CHECK(role IN ('admin', 'user')) NOT NULL
);

-- Create Teams Table (For PPT Evaluation)
CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT NOT NULL,
    problem_id TEXT NOT NULL,
    domain TEXT NOT NULL,
    ppt_path TEXT NOT NULL,
    relevance INTEGER DEFAULT NULL,
    innovation INTEGER DEFAULT NULL,
    usefulness INTEGER DEFAULT NULL,
    originality INTEGER DEFAULT NULL,
    feasibility INTEGER DEFAULT NULL,
    future_scope INTEGER DEFAULT NULL,
    sustainability INTEGER DEFAULT NULL,
    presentation INTEGER DEFAULT NULL,
    judges_opinion_score INTEGER DEFAULT NULL,
    flag TEXT NOT NULL CHECK(flag IN ('Red', 'Orange', 'Green'))
);
