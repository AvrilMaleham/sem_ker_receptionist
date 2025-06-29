-- migrate:up
insert into customer (first_name,last_name,address,phone_number,email,card_num) 
values
('Avril','Maleham','1 beach st, Takapuna','0273100001','director@avjstudio.com','5246123423450987'),
('Vijay','Srinivasan','1 hill st, Onetreehill','0273100002','ceo@avjstudio.com','5246123423450988'),
('Surya','Kakanadan','1 lake st, Tekepo','0273100003','cdo@avjstudio.com','52461234234509879'),
('Chakshita','Shetty','1 gold st, Mumbai','0273100004','coo@avjstudio.com','52461234234509890'),
('Prashanti','Gouru','1 gym st, les mills','0273100005','cso@avjstudio.com','5246123423450891');

insert into staff (first_name,last_name,address,phone_number,email,staff_type)
values
('Jane','Doe',null,null,'jane.doe@avjsalon.com','Receptionist'),
('John','Dane',null,null,'john.dane@avjsalon.com','junior_stylist'),
('someone','blahblah',null,null,'someone.blah@avjsalon.com','senior_stylist'),
('thatone','bluhbluh',null,null,'thatone.bluh@avjsalon.com','expert_stylist');

insert into service (name,cost,duration)
values
('Women Haircut', 80, '60 mins'),
('Men Haircut', 45, '30 mins'),
('Children Cut', 30, '25 mins'),
('Blow Wave or Styling', 60, '45 mins'),
('Hair Colour (Root Touch-up)', 100, '75 mins'),
('Full Colour', 145, '105 mins'),
('Highlights (Half Head)', 150, '105 mins'),
('Highlights (Full Head)', 215, '150 mins'),
('Balayage', 285, '180 mins'),
('Keratin Smoothing', 325, '150 mins'),
('Hair Treatment', 40, '25 mins'),
('Classic Manicure', 40, '35 mins'),
('Gel Manicure', 60, '50 mins'),
('Acrylic Nails (Full Set)', 80, '75 mins'),
('Nail Art (Add-on)', 20, '15 mins'),
('Pedicure', 70, '55 mins'),
('Express Facial', 60, '30 mins'),
('Deluxe Facial', 120, '60 mins'),
('Eyebrow Shaping', 25, '15 mins'),
('Eyebrow Tint', 22, '15 mins'),
('Lash Lift + Tint', 80, '45 mins'),
('Full Body Wax', 150, '75 mins'),
('Brazilian Wax', 65, '35 mins'),
('Day Makeup', 85, '40 mins'),
('Glam/Evening Makeup', 125, '60 mins'),
('Bridal Hair & Makeup', 450, '150 mins'),
('Scalp Massage (Add-on)', 15, '10 mins'),
('Olaplex Treatment (Add-on)', 40, '20 mins'),
('Toner (Add-on to colour)', 38, '20 mins'),
('Fringe/Bangs Trim', 12, '10 mins');



-- migrate:down

