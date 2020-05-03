-- Table: public.soluciones

-- DROP TABLE public.soluciones;

CREATE TABLE eight_queens_puzzle.public.soluciones
(
    id serial NOT NULL,
    solucion character(500) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT soluciones_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.soluciones
    OWNER to postgres;