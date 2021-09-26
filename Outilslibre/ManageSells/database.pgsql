--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: products; Type: TABLE; Schema: public; Owner: komlan
--

CREATE TABLE public.products (
    id integer NOT NULL,
    product_name character varying NOT NULL,
    quantity integer NOT NULL,
    unit_purchase_price integer NOT NULL,
    unit_sels_price integer NOT NULL,
    date timestamp without time zone NOT NULL
);


ALTER TABLE public.products OWNER TO komlan;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: komlan
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_id_seq OWNER TO komlan;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: komlan
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: products_sels; Type: TABLE; Schema: public; Owner: komlan
--

CREATE TABLE public.products_sels (
    id integer NOT NULL,
    date timestamp without time zone NOT NULL,
    client_name character varying,
    quantity integer NOT NULL,
    product_name character varying NOT NULL,
    unit_sels_price integer NOT NULL
);


ALTER TABLE public.products_sels OWNER TO komlan;

--
-- Name: products_sels_id_seq; Type: SEQUENCE; Schema: public; Owner: komlan
--

CREATE SEQUENCE public.products_sels_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_sels_id_seq OWNER TO komlan;

--
-- Name: products_sels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: komlan
--

ALTER SEQUENCE public.products_sels_id_seq OWNED BY public.products_sels.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: komlan
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying NOT NULL,
    identifier character varying NOT NULL,
    password character varying NOT NULL,
    category character varying NOT NULL
);


ALTER TABLE public.users OWNER TO komlan;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: komlan
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO komlan;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: komlan
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: komlan
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Name: products_sels id; Type: DEFAULT; Schema: public; Owner: komlan
--

ALTER TABLE ONLY public.products_sels ALTER COLUMN id SET DEFAULT nextval('public.products_sels_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: komlan
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: komlan
--

COPY public.products (id, product_name, quantity, unit_purchase_price, unit_sels_price, date) FROM stdin;
1	stylo	40	3	5	2020-10-31 21:18:15.30584
2	cahier	23	10	15	2020-11-01 09:50:41.482662
3	crayon	30	3	4	2020-11-01 09:51:13.263069
\.


--
-- Data for Name: products_sels; Type: TABLE DATA; Schema: public; Owner: komlan
--

COPY public.products_sels (id, date, client_name, quantity, product_name, unit_sels_price) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: komlan
--

COPY public.users (id, username, identifier, password, category) FROM stdin;
1	Jean-Marie	komkan	dakomaje	Caissier
2	Jean	komlan	dakomaje	Manager
3	Jo	ji	dak	Caissier
4	John	jean	kom	Caissier
5	John	jean1	koml	Manager
\.


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: komlan
--

SELECT pg_catalog.setval('public.products_id_seq', 3, true);


--
-- Name: products_sels_id_seq; Type: SEQUENCE SET; Schema: public; Owner: komlan
--

SELECT pg_catalog.setval('public.products_sels_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: komlan
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: komlan
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: products_sels products_sels_pkey; Type: CONSTRAINT; Schema: public; Owner: komlan
--

ALTER TABLE ONLY public.products_sels
    ADD CONSTRAINT products_sels_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: komlan
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

