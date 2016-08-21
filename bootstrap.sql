-- For initial creating database

-- DROP TABLE public.user_visits;
CREATE TABLE public.user_visits
(
  id SERIAL PRIMARY KEY,
  user_id UUID NOT NULL,
  page text NOT NULL,
  useragent text NOT NULL,
  ip inet NOT NULL
);

-- DROP TABLE public.user_data;
CREATE TABLE public.user_data
(
  id SERIAL PRIMARY KEY,
  user_id UUID NOT NULL,
  action_type INT NOT NULL,
  action_name TEXT NOT NULL,
  action_value TEXT
);
CREATE INDEX user_data_action_type_index ON public.user_data (action_type);
