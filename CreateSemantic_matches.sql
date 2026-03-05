CREATE TABLE semantic_matches (
    id SERIAL PRIMARY KEY,
    texto_origem TEXT NOT NULL,
    texto_normalizado TEXT NOT NULL,
    produto_id INT REFERENCES products(id),
    confianca FLOAT,
    validado_humano BOOLEAN DEFAULT TRUE,
    criado_em TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_semantic_matches_normalizado ON semantic_matches (texto_normalizado);