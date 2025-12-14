-- WARNING: This schema is for context only and is not meant to be run.
-- Table order and constraints may not be valid for execution.

CREATE TABLE public.customers (
  customer_id uuid NOT NULL DEFAULT gen_random_uuid(),
  name character varying NOT NULL,
  phone character varying NOT NULL,
  category text NOT NULL,
  address character varying NOT NULL,
  created_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  updated_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  CONSTRAINT customers_pkey PRIMARY KEY (customer_id)
);

CREATE TABLE public.product_categories (
  category_id text NOT NULL,
  category_name text NOT NULL,
  created_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  updated_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  CONSTRAINT product_categories_pkey PRIMARY KEY (category_id)
);

CREATE TABLE public.product_images (
  image_id uuid NOT NULL DEFAULT gen_random_uuid(),
  product_id uuid NOT NULL DEFAULT gen_random_uuid(),
  image_url character varying NOT NULL,
  order_index integer,
  created_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  updated_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  CONSTRAINT product_images_pkey PRIMARY KEY (image_id),
  CONSTRAINT product_images_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product_items(product_id)
);

CREATE TABLE public.product_items (
  product_id uuid NOT NULL DEFAULT gen_random_uuid(),
  state text NOT NULL,
  sku character varying NOT NULL,
  model uuid NOT NULL DEFAULT gen_random_uuid(),
  storage bigint,
  colour character varying,
  physical text NOT NULL,
  warranty_type character varying,
  warranty_state text NOT NULL,
  package character varying NOT NULL,
  condition character varying NOT NULL,
  defect character varying NOT NULL,
  created_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  updated_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  CONSTRAINT product_items_pkey PRIMARY KEY (product_id),
  CONSTRAINT product_items_model_fkey FOREIGN KEY (model) REFERENCES public.product_models(product_model_id)
);

CREATE TABLE public.product_models (
  product_model_id uuid NOT NULL DEFAULT gen_random_uuid(),
  category_id text NOT NULL,
  brand text NOT NULL,
  model_name character varying NOT NULL,
  production_year integer NOT NULL,
  created_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  updated_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  CONSTRAINT product_models_pkey PRIMARY KEY (product_model_id),
  CONSTRAINT products_models_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.product_categories(category_id)
);

CREATE TABLE public.purchases (
  purchase_id uuid NOT NULL DEFAULT gen_random_uuid(),
  customer_id uuid NOT NULL DEFAULT gen_random_uuid(),
  date date NOT NULL,
  location character varying NOT NULL,
  transportation_cost integer NOT NULL,
  bonus character varying,
  created_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  updated_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  CONSTRAINT purchases_pkey PRIMARY KEY (purchase_id),
  CONSTRAINT purchases_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id)
);

CREATE TABLE public.purchases_items (
  product_id uuid NOT NULL DEFAULT gen_random_uuid(),
  purchase_id uuid NOT NULL DEFAULT gen_random_uuid(),
  price integer NOT NULL,
  additional_cost integer NOT NULL,
  cost_description character varying NOT NULL,
  created_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  updated_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  CONSTRAINT purchases_items_pkey PRIMARY KEY (product_id),
  CONSTRAINT purchases_products_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product_items(product_id),
  CONSTRAINT purchases_products_purchase_id_fkey FOREIGN KEY (purchase_id) REFERENCES public.purchases(purchase_id)
);

CREATE TABLE public.sales (
  sales_id uuid NOT NULL DEFAULT gen_random_uuid(),
  customer_id uuid NOT NULL DEFAULT gen_random_uuid(),
  date date NOT NULL,
  location character varying NOT NULL,
  transportation_cost integer NOT NULL,
  bonus character varying NOT NULL,
  created_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  updated_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  CONSTRAINT sales_pkey PRIMARY KEY (sales_id),
  CONSTRAINT sales_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(customer_id)
);

CREATE TABLE public.sales_items (
  product_id uuid NOT NULL DEFAULT gen_random_uuid(),
  sales_id uuid NOT NULL DEFAULT gen_random_uuid(),
  price integer NOT NULL,
  additional_cost integer NOT NULL,
  description_cost character varying NOT NULL,
  created_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  updated_at timestamp with time zone NOT NULL DEFAULT (now() AT TIME ZONE 'utc'::text),
  CONSTRAINT sales_items_pkey PRIMARY KEY (product_id),
  CONSTRAINT sales_items_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product_items(product_id),
  CONSTRAINT sales_items_sales_id_fkey FOREIGN KEY (sales_id) REFERENCES public.sales(sales_id)
);