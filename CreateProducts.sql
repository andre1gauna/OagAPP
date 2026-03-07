CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    sku TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    texto_canonico TEXT NOT NULL,
    atributos JSONB,
    preco NUMERIC(12,2),
    unidade TEXT,
    ativo BOOLEAN DEFAULT TRUE,
    criado_em TIMESTAMP DEFAULT NOW()
);

-- busca full text
CREATE INDEX idx_products_texto_canonico 
ON products USING GIN (to_tsvector('simple', texto_canonico));

-- busca em JSON
CREATE INDEX idx_products_atributos 
ON products USING GIN (atributos);

-- 🔹 novo índice trigram para ILIKE
CREATE INDEX idx_products_texto_trgm 
ON products USING GIN (texto_canonico gin_trgm_ops);