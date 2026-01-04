-- Table: public.images

-- DROP TABLE IF EXISTS public.images;

CREATE TABLE IF NOT EXISTS public.images
(
    id integer NOT NULL DEFAULT nextval('images_id_seq'::regclass),
    filename text COLLATE pg_catalog."default",
    sha256 text COLLATE pg_catalog."default" NOT NULL,
    phash bigint,
    embedding double precision[],
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT images_pkey PRIMARY KEY (id),
    CONSTRAINT images_sha256_key UNIQUE (sha256)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.images
    OWNER to postgres;