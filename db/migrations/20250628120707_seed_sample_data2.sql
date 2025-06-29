-- migrate:up

UPDATE service SET skill_level = 'expert' WHERE name IN (
  'Women Haircut',
  'Hair Colour (Root Touch-up)',
  'Full Colour',
  'Highlights (Half Head)',
  'Highlights (Full Head)',
  'Balayage',
  'Keratin Smoothing',
  'Bridal Hair & Makeup'
);

UPDATE service SET skill_level = 'intermediate' WHERE name IN (
  'Men Haircut',
  'Blow Wave or Styling',
  'Hair Treatment',
  'Gel Manicure',
  'Acrylic Nails (Full Set)',
  'Pedicure',
  'Deluxe Facial',
  'Lash Lift + Tint',
  'Full Body Wax',
  'Brazilian Wax',
  'Glam/Evening Makeup',
  'Toner (Add-on to colour)',
  'Olaplex Treatment (Add-on)'
);

UPDATE service SET skill_level = 'junior' WHERE name IN (
  'Children Cut',
  'Classic Manicure',
  'Nail Art (Add-on)',
  'Express Facial',
  'Eyebrow Shaping',
  'Eyebrow Tint',
  'Day Makeup',
  'Scalp Massage (Add-on)',
  'Fringe/Bangs Trim'
);


-- migrate:down

