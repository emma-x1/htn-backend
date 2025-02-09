CREATE TABLE hackers (
    badge_code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER update_hackers_timestamp
AFTER UPDATE ON hackers
FOR EACH ROW
BEGIN
    UPDATE hackers SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;


--
-- LEARNING SCRIPTS
--

-- ALTER TABLE <tablename> ADD COLUMN status TEXT;

-- DROP TABLE <tablename>;

-- INSERT INTO hackers (badge_code, name, email, phone) VALUES ('1234', 'John Doe', '

-- SELECT * FROM hackers
-- LIMIT 2;

-- UPDATE hackers SET name = 'Jane Doe' WHERE badge_code = '1234';

-- DELETE FROM hackers WHERE badge_code = '1234';

-- CREATE TABLE scans (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    badge_code TEXT REFERENCES hackers(badge_code),
--    activity_name TEXT NOT NULL,
--    activity_category TEXT NOT NULL,
--    scanned_at DATETIME DEFAULT CURRENT_TIMESTAMP
--);

-- CREATE VIEW scan_activity AS
--      SELECT * FROM scans s
--      JOIN hackers h ON s.badge_code = h.badge_code;

-- SELECT * FROM scan_activity;
