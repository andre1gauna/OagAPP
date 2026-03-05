CREATE TABLE term_equivalences (
    id SERIAL PRIMARY KEY,
    conceito TEXT NOT NULL,
    termo TEXT NOT NULL,
    normalizado TEXT NOT NULL,
    categoria TEXT,
    fonte TEXT,
    observacao TEXT
);

CREATE INDEX idx_term_equivalences_termo ON term_equivalences (termo);