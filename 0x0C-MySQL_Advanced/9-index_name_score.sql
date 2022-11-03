--  idx_name_first_score
create index idx_name_first_score ON names (name(1), score);