--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5 (Ubuntu 15.5-0ubuntu0.23.04.1)
-- Dumped by pg_dump version 15.5 (Ubuntu 15.5-0ubuntu0.23.04.1)

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

--
-- Name: final; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA final;


ALTER SCHEMA final OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: copper; Type: TABLE; Schema: final; Owner: postgres
--

CREATE TABLE final.copper (
    date character varying NOT NULL,
    open double precision,
    close double precision,
    high double precision,
    low double precision,
    volume integer
);


ALTER TABLE final.copper OWNER TO postgres;

--
-- Name: gold; Type: TABLE; Schema: final; Owner: postgres
--

CREATE TABLE final.gold (
    date character varying NOT NULL,
    open double precision,
    close double precision,
    high double precision,
    low double precision,
    volume integer
);


ALTER TABLE final.gold OWNER TO postgres;

--
-- Name: palladium; Type: TABLE; Schema: final; Owner: postgres
--

CREATE TABLE final.palladium (
    date character varying NOT NULL,
    open double precision,
    close double precision,
    high double precision,
    low double precision,
    volume integer
);


ALTER TABLE final.palladium OWNER TO postgres;

--
-- Name: platinum; Type: TABLE; Schema: final; Owner: postgres
--

CREATE TABLE final.platinum (
    date character varying NOT NULL,
    open double precision,
    close double precision,
    high double precision,
    low double precision,
    volume integer
);


ALTER TABLE final.platinum OWNER TO postgres;

--
-- Name: predictions; Type: TABLE; Schema: final; Owner: postgres
--

CREATE TABLE final.predictions (
    id integer NOT NULL,
    metal character varying,
    algorithm character varying,
    prediction double precision,
    predicted_date character varying,
    generated_at character varying
);


ALTER TABLE final.predictions OWNER TO postgres;

--
-- Name: predictions_id_seq; Type: SEQUENCE; Schema: final; Owner: postgres
--

CREATE SEQUENCE final.predictions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE final.predictions_id_seq OWNER TO postgres;

--
-- Name: predictions_id_seq; Type: SEQUENCE OWNED BY; Schema: final; Owner: postgres
--

ALTER SEQUENCE final.predictions_id_seq OWNED BY final.predictions.id;


--
-- Name: silver; Type: TABLE; Schema: final; Owner: postgres
--

CREATE TABLE final.silver (
    date character varying NOT NULL,
    open double precision,
    close double precision,
    high double precision,
    low double precision,
    volume integer
);


ALTER TABLE final.silver OWNER TO postgres;

--
-- Name: statistics; Type: TABLE; Schema: final; Owner: postgres
--

CREATE TABLE final.statistics (
    id integer NOT NULL,
    metal character varying,
    stat_type character varying,
    value double precision,
    start_date character varying,
    end_date character varying,
    generated_at character varying,
    "column" character varying
);


ALTER TABLE final.statistics OWNER TO postgres;

--
-- Name: statistics_id_seq; Type: SEQUENCE; Schema: final; Owner: postgres
--

CREATE SEQUENCE final.statistics_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE final.statistics_id_seq OWNER TO postgres;

--
-- Name: statistics_id_seq; Type: SEQUENCE OWNED BY; Schema: final; Owner: postgres
--

ALTER SEQUENCE final.statistics_id_seq OWNED BY final.statistics.id;


--
-- Name: visualizations; Type: TABLE; Schema: final; Owner: postgres
--

CREATE TABLE final.visualizations (
    id integer NOT NULL,
    metal character varying,
    visual_type character varying,
    parameters json,
    file_path character varying,
    generated_at character varying
);


ALTER TABLE final.visualizations OWNER TO postgres;

--
-- Name: visualizations_id_seq; Type: SEQUENCE; Schema: final; Owner: postgres
--

CREATE SEQUENCE final.visualizations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE final.visualizations_id_seq OWNER TO postgres;

--
-- Name: visualizations_id_seq; Type: SEQUENCE OWNED BY; Schema: final; Owner: postgres
--

ALTER SEQUENCE final.visualizations_id_seq OWNED BY final.visualizations.id;


--
-- Name: predictions id; Type: DEFAULT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.predictions ALTER COLUMN id SET DEFAULT nextval('final.predictions_id_seq'::regclass);


--
-- Name: statistics id; Type: DEFAULT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.statistics ALTER COLUMN id SET DEFAULT nextval('final.statistics_id_seq'::regclass);


--
-- Name: visualizations id; Type: DEFAULT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.visualizations ALTER COLUMN id SET DEFAULT nextval('final.visualizations_id_seq'::regclass);


--
-- Name: copper copper_pkey; Type: CONSTRAINT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.copper
    ADD CONSTRAINT copper_pkey PRIMARY KEY (date);


--
-- Name: gold gold_pkey; Type: CONSTRAINT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.gold
    ADD CONSTRAINT gold_pkey PRIMARY KEY (date);


--
-- Name: palladium palladium_pkey; Type: CONSTRAINT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.palladium
    ADD CONSTRAINT palladium_pkey PRIMARY KEY (date);


--
-- Name: platinum platinum_pkey; Type: CONSTRAINT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.platinum
    ADD CONSTRAINT platinum_pkey PRIMARY KEY (date);


--
-- Name: predictions predictions_pkey; Type: CONSTRAINT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.predictions
    ADD CONSTRAINT predictions_pkey PRIMARY KEY (id);


--
-- Name: silver silver_pkey; Type: CONSTRAINT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.silver
    ADD CONSTRAINT silver_pkey PRIMARY KEY (date);


--
-- Name: statistics statistics_pkey; Type: CONSTRAINT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.statistics
    ADD CONSTRAINT statistics_pkey PRIMARY KEY (id);


--
-- Name: visualizations visualizations_pkey; Type: CONSTRAINT; Schema: final; Owner: postgres
--

ALTER TABLE ONLY final.visualizations
    ADD CONSTRAINT visualizations_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

