insert into bangazonapi_recommendation (id, customer_id, product_id, recommender_id)
    values (1, 1, 1, 2);
insert into bangazonapi_recommendation (id, customer_id, product_id, recommender_id)
    values (2, 2, 1, 1);
insert into bangazonapi_recommendation (id, customer_id, product_id, recommender_id)
    values (3, 1, 1, 4);
insert into bangazonapi_recommendation (id, customer_id, product_id, recommender_id)
    values (4, 4, 1, 1);
insert into bangazonapi_recommendation (id, customer_id, product_id, recommender_id)
    values (5, 5, 1, 6);
insert into bangazonapi_recommendation (id, customer_id, product_id, recommender_id)
    values (6, 6, 1, 5);
insert into bangazonapi_recommendation (id, customer_id, product_id, recommender_id)
    values (7, 4, 1, 5);
insert into bangazonapi_recommendation (id, customer_id, product_id, recommender_id)
    values (8, 5, 1, 4);
DELETE FROM bangazonapi_recommendation
    WHERE customer_id = 1;
DELETE FROM bangazonapi_recommendation
    WHERE recommender_id = 1;