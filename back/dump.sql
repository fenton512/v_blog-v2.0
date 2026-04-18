--
-- PostgreSQL database cluster dump
--

\restrict JZyHb9j5TIvzlWZw5zoAnIqHS4qoBpRtyNzcjnR1yXjiNF5meYRfbuBxMPgXPyM

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--

DROP DATABASE vector_blog;




--
-- Drop roles
--

DROP ROLE vector;


--
-- Roles
--

CREATE ROLE vector;
ALTER ROLE vector WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:+iULI5JS1xVtBKVfZbkz3g==$5g4xnue3zCLCoi3VaPnL04As/esKNOLijEwvMH7pE6k=:BOEr7JL+gIcA8wGirlJ7dpJG+YwvkdL7vunFydkGfMk=';

--
-- User Configurations
--








\unrestrict JZyHb9j5TIvzlWZw5zoAnIqHS4qoBpRtyNzcjnR1yXjiNF5meYRfbuBxMPgXPyM

--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

\restrict DkkeEdYScVP1cvnG8ksAtRcpGvXQwUlMLsUeJHWZvT5CDcip6Mqch2fy4f22maH

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: vector
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO vector;

\unrestrict DkkeEdYScVP1cvnG8ksAtRcpGvXQwUlMLsUeJHWZvT5CDcip6Mqch2fy4f22maH
\connect template1
\restrict DkkeEdYScVP1cvnG8ksAtRcpGvXQwUlMLsUeJHWZvT5CDcip6Mqch2fy4f22maH

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: vector
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: vector
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\unrestrict DkkeEdYScVP1cvnG8ksAtRcpGvXQwUlMLsUeJHWZvT5CDcip6Mqch2fy4f22maH
\connect template1
\restrict DkkeEdYScVP1cvnG8ksAtRcpGvXQwUlMLsUeJHWZvT5CDcip6Mqch2fy4f22maH

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: vector
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

\unrestrict DkkeEdYScVP1cvnG8ksAtRcpGvXQwUlMLsUeJHWZvT5CDcip6Mqch2fy4f22maH

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

\restrict kLXr8MmlpGA8cLrpIbsqzcbA28KjRtebnccYMGUmwGSS7PwT1cg3JT1Kt1qn7Up

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: vector
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO vector;

\unrestrict kLXr8MmlpGA8cLrpIbsqzcbA28KjRtebnccYMGUmwGSS7PwT1cg3JT1Kt1qn7Up
\connect postgres
\restrict kLXr8MmlpGA8cLrpIbsqzcbA28KjRtebnccYMGUmwGSS7PwT1cg3JT1Kt1qn7Up

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: vector
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- PostgreSQL database dump complete
--

\unrestrict kLXr8MmlpGA8cLrpIbsqzcbA28KjRtebnccYMGUmwGSS7PwT1cg3JT1Kt1qn7Up

--
-- Database "vector_blog" dump
--

--
-- PostgreSQL database dump
--

\restrict uQNQZAoznP2K9wPpiRhlgFJGYjKYMJm40d4XOMnJIfXmeCiODaZmN5U0sghC1Il

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: vector_blog; Type: DATABASE; Schema: -; Owner: vector
--

CREATE DATABASE vector_blog WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE vector_blog OWNER TO vector;

\unrestrict uQNQZAoznP2K9wPpiRhlgFJGYjKYMJm40d4XOMnJIfXmeCiODaZmN5U0sghC1Il
\connect vector_blog
\restrict uQNQZAoznP2K9wPpiRhlgFJGYjKYMJm40d4XOMnJIfXmeCiODaZmN5U0sghC1Il

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO vector;

--
-- Name: comments; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.comments (
    id integer NOT NULL,
    text text NOT NULL,
    creation_time timestamp without time zone NOT NULL,
    updating_time timestamp without time zone,
    author_id integer NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE public.comments OWNER TO vector;

--
-- Name: comments_id_seq; Type: SEQUENCE; Schema: public; Owner: vector
--

CREATE SEQUENCE public.comments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.comments_id_seq OWNER TO vector;

--
-- Name: comments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vector
--

ALTER SEQUENCE public.comments_id_seq OWNED BY public.comments.id;


--
-- Name: files; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.files (
    id integer NOT NULL,
    url character varying(30) NOT NULL,
    type character varying(7) NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE public.files OWNER TO vector;

--
-- Name: files_id_seq; Type: SEQUENCE; Schema: public; Owner: vector
--

CREATE SEQUENCE public.files_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.files_id_seq OWNER TO vector;

--
-- Name: files_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vector
--

ALTER SEQUENCE public.files_id_seq OWNED BY public.files.id;


--
-- Name: groups; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.groups (
    id integer NOT NULL,
    name character varying(15) NOT NULL
);


ALTER TABLE public.groups OWNER TO vector;

--
-- Name: groups_id_seq; Type: SEQUENCE; Schema: public; Owner: vector
--

CREATE SEQUENCE public.groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.groups_id_seq OWNER TO vector;

--
-- Name: groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vector
--

ALTER SEQUENCE public.groups_id_seq OWNED BY public.groups.id;


--
-- Name: posts; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    text text NOT NULL,
    creation_time timestamp without time zone NOT NULL,
    updating_time timestamp without time zone,
    author_id integer NOT NULL
);


ALTER TABLE public.posts OWNER TO vector;

--
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: vector
--

CREATE SEQUENCE public.posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.posts_id_seq OWNER TO vector;

--
-- Name: posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vector
--

ALTER SEQUENCE public.posts_id_seq OWNED BY public.posts.id;


--
-- Name: posts_in_group; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.posts_in_group (
    post_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.posts_in_group OWNER TO vector;

--
-- Name: themes; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.themes (
    id integer NOT NULL,
    name character varying NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.themes OWNER TO vector;

--
-- Name: themes_id_seq; Type: SEQUENCE; Schema: public; Owner: vector
--

CREATE SEQUENCE public.themes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.themes_id_seq OWNER TO vector;

--
-- Name: themes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vector
--

ALTER SEQUENCE public.themes_id_seq OWNED BY public.themes.id;


--
-- Name: themes_in_post; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.themes_in_post (
    post_id integer NOT NULL,
    theme_id integer NOT NULL
);


ALTER TABLE public.themes_in_post OWNER TO vector;

--
-- Name: tokens; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.tokens (
    id integer NOT NULL,
    user_id integer NOT NULL,
    family_id integer NOT NULL,
    token_hash character varying NOT NULL,
    is_active boolean NOT NULL,
    expired_at timestamp without time zone NOT NULL
);


ALTER TABLE public.tokens OWNER TO vector;

--
-- Name: tokens_id_seq; Type: SEQUENCE; Schema: public; Owner: vector
--

CREATE SEQUENCE public.tokens_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tokens_id_seq OWNER TO vector;

--
-- Name: tokens_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vector
--

ALTER SEQUENCE public.tokens_id_seq OWNED BY public.tokens.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying NOT NULL,
    nickname character varying(15) NOT NULL,
    role character varying(7) NOT NULL,
    password character varying NOT NULL,
    avatar_url character varying(120),
    is_active boolean NOT NULL,
    description text
);


ALTER TABLE public.users OWNER TO vector;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: vector
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO vector;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vector
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: users_in_group; Type: TABLE; Schema: public; Owner: vector
--

CREATE TABLE public.users_in_group (
    user_id integer NOT NULL,
    groupe_id integer NOT NULL
);


ALTER TABLE public.users_in_group OWNER TO vector;

--
-- Name: comments id; Type: DEFAULT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.comments ALTER COLUMN id SET DEFAULT nextval('public.comments_id_seq'::regclass);


--
-- Name: files id; Type: DEFAULT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.files ALTER COLUMN id SET DEFAULT nextval('public.files_id_seq'::regclass);


--
-- Name: groups id; Type: DEFAULT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.groups ALTER COLUMN id SET DEFAULT nextval('public.groups_id_seq'::regclass);


--
-- Name: posts id; Type: DEFAULT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.posts ALTER COLUMN id SET DEFAULT nextval('public.posts_id_seq'::regclass);


--
-- Name: themes id; Type: DEFAULT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.themes ALTER COLUMN id SET DEFAULT nextval('public.themes_id_seq'::regclass);


--
-- Name: tokens id; Type: DEFAULT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.tokens ALTER COLUMN id SET DEFAULT nextval('public.tokens_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.alembic_version (version_num) FROM stdin;
dd9768fb9451
\.


--
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.comments (id, text, creation_time, updating_time, author_id, post_id) FROM stdin;
1	вот мой коммент типа, да	2026-04-12 17:38:11.777731	\N	1	1
\.


--
-- Data for Name: files; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.files (id, url, type, post_id) FROM stdin;
\.


--
-- Data for Name: groups; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.groups (id, name) FROM stdin;
\.


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.posts (id, text, creation_time, updating_time, author_id) FROM stdin;
1	this is my first post	2026-04-12 17:26:50.794624	\N	1
2	а это мой второй пост	2026-04-12 17:28:32.440481	\N	1
3	а это мой новый, третий пост	2026-04-15 16:22:22.597928	\N	1
\.


--
-- Data for Name: posts_in_group; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.posts_in_group (post_id, group_id) FROM stdin;
\.


--
-- Data for Name: themes; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.themes (id, name, is_active) FROM stdin;
1	test	t
\.


--
-- Data for Name: themes_in_post; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.themes_in_post (post_id, theme_id) FROM stdin;
1	1
2	1
3	1
\.


--
-- Data for Name: tokens; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.tokens (id, user_id, family_id, token_hash, is_active, expired_at) FROM stdin;
1	1	1	cc7b2652e6c0bbb77fe966775ff2e44b5cf779bb9ca48eb07040c2a8c62f0c4f	f	2026-04-27 15:40:26.052294
2	1	1	974521b5315b82dbcec23bbdc4619e9fe978aac6bcd014ddc852a0a8aec99861	f	2026-04-27 17:20:26.303272
3	1	1	06580cb293cfa0bd4dc6f83dcbd4b512cd26c9bccee13948030410a9bd7ad41d	f	2026-04-27 17:22:24.916571
4	1	1	14f248262ab54ffa182f3c44f7f62676012592a010f1158686ba958522021463	f	2026-04-27 17:26:29.885477
5	1	1	3f2adff5d67b3dd5f6addaec70680f2d9ffecfe63ed5986b2a2958e9cadca6c4	f	2026-04-27 18:56:34.437903
6	1	1	8f2113633421af7626560786df6b52413b9f6109c3f7f3a7f315d9f59df00e2e	f	2026-04-27 19:02:50.93375
7	1	1	f1ed21ce4edddb6f27b4869291489f3bfd35b50cb88b44601701d9c58e8b750e	f	2026-04-27 19:07:50.703861
8	1	1	0d3c037b577dc4491fe3527a04fd8c9443e46223b8b62dd71368ab6de11add8f	f	2026-04-27 19:09:31.777324
9	1	1	821490198cef3f17480f8908c6f452cb533f347605e5a16e6f8df7a26ea0513a	f	2026-04-27 19:13:00.114288
10	1	1	c530533ce1c0fd2de7e4d43f7a25711e0cd4ffa9f389759d4d07ce2251584e9f	f	2026-04-27 20:25:24.30088
11	1	1	426fddeed90113c47776d1b6db6a31f9f5bc1249d790c9a354a4ea82bac4dd14	f	2026-04-29 17:42:10.633694
12	1	1	e1e5d0f372fe3e0fff28e94f7084bd652c3805f586fcafcb87c8462315ea9610	f	2026-04-29 17:42:54.063108
13	1	1	f72322a2c821cd7730776a466093b36fbb823457d1d4544f114883479fdf4fed	f	2026-04-29 17:43:26.165777
14	1	1	98ca4a4db186d366cee469895c88372cd6a9303e1bfa8aa00d3c8354d1f0cf9f	f	2026-04-29 17:50:13.659549
15	1	1	40b8e91108a5c418818173532e24e9bf6595e53e49e3644644dc761dd8fc9e2e	f	2026-04-29 17:50:31.481265
16	1	1	158635377e26b440a4cbaf71743b3a575e772591fea9c54172ef28eb7da29c98	f	2026-04-29 18:15:14.913119
17	1	1	1d71af483f9956ee700e2a1e870a6c8c2191b0bbdb17cfe2866f9348e2af4894	f	2026-04-29 18:15:50.085471
18	1	1	4e33ef572aa3c1825a3ef11224143eaf25f0d376705ec036a3d6f9bf70ac9e60	f	2026-04-29 18:19:49.642027
19	1	1	794a7941b482afb62f9b78ad994a48a32c9a161311ae0818b3a228eb6d28109e	f	2026-04-29 18:37:46.553735
20	1	1	fd51821c794e92f358000c2cba0fac6c6383af92f225fc9149c3e11d212cdc59	f	2026-04-30 10:05:44.981321
21	1	1	b6842a72fb77dcd24a31518055ae3ee597e1d9409238829b3c15126c289084c1	f	2026-04-30 10:09:37.729224
22	1	1	23656155057292b6cd696adf4761298a4e938f30430da6d68c2b7b0973aa65c6	f	2026-04-30 10:13:29.08585
23	1	1	fda78f369f4267d6f858b94abf612d9127f71d14d7cff6f17ef2105e0beecc19	f	2026-04-30 10:39:18.537124
24	1	1	81cdfb2f617c38614f65f63e2e256c22638a7b2ca6a13d7a2b6f05af0f179f86	f	2026-04-30 10:44:56.120186
25	1	1	654340269fc566e817222dfd3f814d674b09458b9530e3270ea85818e31adfa8	f	2026-04-30 10:45:06.631098
26	1	1	f26a64bfbd0de91bc415e03057ea4f7de53742a91b24caf6cee2e9ddbff2aa9d	f	2026-04-30 10:52:20.431103
27	1	1	48e35fd43a3ea4bc1ff7ca085e7d58fa8a874ff1a68ca883e8852d982ecc1b66	f	2026-04-30 10:52:22.948878
28	1	1	5ad86eda61105be941a8d1cbe0889ce977cc57916d1e013fdb5b3a2153f44277	f	2026-04-30 10:53:12.306292
29	1	1	ac205639202806f7251be2965896e3c69491c401bb637f2ce7d3bc3c63b96bf9	f	2026-04-30 11:16:42.903909
30	1	1	efeb159d06631ea5bc92bcf5409cac54cf59c4f86bb6153831ec8bfb318fb4e0	t	2026-04-30 16:22:22.468495
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.users (id, email, nickname, role, password, avatar_url, is_active, description) FROM stdin;
1	123@mail.ru	234klj	admin	$2b$12$q9LaGa8oBSHw5CSOHCYJe.1L.366r9mqazxmMRBOAJxogZ9odrCpy	\N	t	\N
\.


--
-- Data for Name: users_in_group; Type: TABLE DATA; Schema: public; Owner: vector
--

COPY public.users_in_group (user_id, groupe_id) FROM stdin;
\.


--
-- Name: comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vector
--

SELECT pg_catalog.setval('public.comments_id_seq', 1, true);


--
-- Name: files_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vector
--

SELECT pg_catalog.setval('public.files_id_seq', 1, false);


--
-- Name: groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vector
--

SELECT pg_catalog.setval('public.groups_id_seq', 1, false);


--
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vector
--

SELECT pg_catalog.setval('public.posts_id_seq', 3, true);


--
-- Name: themes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vector
--

SELECT pg_catalog.setval('public.themes_id_seq', 1, true);


--
-- Name: tokens_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vector
--

SELECT pg_catalog.setval('public.tokens_id_seq', 30, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vector
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (id);


--
-- Name: files files_id_key; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.files
    ADD CONSTRAINT files_id_key UNIQUE (id);


--
-- Name: files files_pkey; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.files
    ADD CONSTRAINT files_pkey PRIMARY KEY (id);


--
-- Name: files files_url_key; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.files
    ADD CONSTRAINT files_url_key UNIQUE (url);


--
-- Name: groups groups_name_key; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_name_key UNIQUE (name);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (id);


--
-- Name: posts_in_group posts_in_group_pkey; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.posts_in_group
    ADD CONSTRAINT posts_in_group_pkey PRIMARY KEY (post_id, group_id);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- Name: themes themes_id_key; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.themes
    ADD CONSTRAINT themes_id_key UNIQUE (id);


--
-- Name: themes_in_post themes_in_post_pkey; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.themes_in_post
    ADD CONSTRAINT themes_in_post_pkey PRIMARY KEY (post_id, theme_id);


--
-- Name: themes themes_pkey; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.themes
    ADD CONSTRAINT themes_pkey PRIMARY KEY (id);


--
-- Name: tokens tokens_pkey; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.tokens
    ADD CONSTRAINT tokens_pkey PRIMARY KEY (id);


--
-- Name: users_in_group users_in_group_pkey; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.users_in_group
    ADD CONSTRAINT users_in_group_pkey PRIMARY KEY (user_id, groupe_id);


--
-- Name: users users_password_key; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_password_key UNIQUE (password);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_comments_author_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_comments_author_id ON public.comments USING btree (author_id);


--
-- Name: ix_comments_creation_time; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_comments_creation_time ON public.comments USING btree (creation_time);


--
-- Name: ix_comments_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_comments_id ON public.comments USING btree (id);


--
-- Name: ix_comments_post_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_comments_post_id ON public.comments USING btree (post_id);


--
-- Name: ix_files_post_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_files_post_id ON public.files USING btree (post_id);


--
-- Name: ix_files_type; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_files_type ON public.files USING btree (type);


--
-- Name: ix_groups_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_groups_id ON public.groups USING btree (id);


--
-- Name: ix_posts_creation_time; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_posts_creation_time ON public.posts USING btree (creation_time);


--
-- Name: ix_posts_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_posts_id ON public.posts USING btree (id);


--
-- Name: ix_posts_in_group_group_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_posts_in_group_group_id ON public.posts_in_group USING btree (group_id);


--
-- Name: ix_posts_in_group_post_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_posts_in_group_post_id ON public.posts_in_group USING btree (post_id);


--
-- Name: ix_themes_in_post_post_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_themes_in_post_post_id ON public.themes_in_post USING btree (post_id);


--
-- Name: ix_themes_in_post_theme_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_themes_in_post_theme_id ON public.themes_in_post USING btree (theme_id);


--
-- Name: ix_themes_name; Type: INDEX; Schema: public; Owner: vector
--

CREATE UNIQUE INDEX ix_themes_name ON public.themes USING btree (name);


--
-- Name: ix_tokens_token_hash; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_tokens_token_hash ON public.tokens USING btree (token_hash);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: vector
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: ix_users_in_group_groupe_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_users_in_group_groupe_id ON public.users_in_group USING btree (groupe_id);


--
-- Name: ix_users_in_group_user_id; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_users_in_group_user_id ON public.users_in_group USING btree (user_id);


--
-- Name: ix_users_is_active; Type: INDEX; Schema: public; Owner: vector
--

CREATE INDEX ix_users_is_active ON public.users USING btree (is_active);


--
-- Name: ix_users_nickname; Type: INDEX; Schema: public; Owner: vector
--

CREATE UNIQUE INDEX ix_users_nickname ON public.users USING btree (nickname);


--
-- Name: comments comments_author_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.users(id);


--
-- Name: comments comments_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- Name: files files_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.files
    ADD CONSTRAINT files_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- Name: posts posts_author_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.users(id);


--
-- Name: posts_in_group posts_in_group_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.posts_in_group
    ADD CONSTRAINT posts_in_group_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.groups(id) ON DELETE CASCADE;


--
-- Name: posts_in_group posts_in_group_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.posts_in_group
    ADD CONSTRAINT posts_in_group_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(id) ON DELETE CASCADE;


--
-- Name: themes_in_post themes_in_post_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.themes_in_post
    ADD CONSTRAINT themes_in_post_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(id) ON DELETE CASCADE;


--
-- Name: themes_in_post themes_in_post_theme_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.themes_in_post
    ADD CONSTRAINT themes_in_post_theme_id_fkey FOREIGN KEY (theme_id) REFERENCES public.themes(id) ON DELETE CASCADE;


--
-- Name: tokens tokens_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.tokens
    ADD CONSTRAINT tokens_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: users_in_group users_in_group_groupe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.users_in_group
    ADD CONSTRAINT users_in_group_groupe_id_fkey FOREIGN KEY (groupe_id) REFERENCES public.groups(id) ON DELETE CASCADE;


--
-- Name: users_in_group users_in_group_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vector
--

ALTER TABLE ONLY public.users_in_group
    ADD CONSTRAINT users_in_group_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

\unrestrict uQNQZAoznP2K9wPpiRhlgFJGYjKYMJm40d4XOMnJIfXmeCiODaZmN5U0sghC1Il

--
-- PostgreSQL database cluster dump complete
--

