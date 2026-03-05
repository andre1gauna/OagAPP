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

CREATE INDEX idx_products_texto_canonico ON products USING GIN (to_tsvector('simple', texto_canonico));
CREATE INDEX idx_products_atributos ON products USING GIN (atributos);