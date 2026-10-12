# Updated README: column mapping and category codes

This project now follows the following column conventions (Excel-style):

- Columns A and B: metadata (NOT used as inputs)
- AD: Y1 (binary printability flag)
- AE: Y2 (printability class: 0/1/2)
- AF-AI: Y3 (four continuous texture properties)

Categorical/encoded factors present as integer codes in the dataset:

- colloid_type: 1=CaCl2, 2=NaCl, 3=urea

- starch_type:
  1: Corn starch
  2: Tapioca starch
  3: Glutinous rice
  4: Japonica rice
  5: Indica rice
  6: Hylon 4
  7: Potato starch
  8: Wheat
  9: Waxy corn starch
  10: Pregelatinized waxy corn starch
  11: Rice starch
  12: Red cabbage
  13: Sweet potato
  14: Cassava
  15: Mung bean
  16: Pea
  17: Red sweet potato
  18: Buckwheat

- hydrocolloid_type:
  1: Sodium alginate
  2: Sodium alginate + LMP
  3: Xanthan gum
  4: Sodium alginate + xanthan gum
  5: Carrageenan
  6: Gum arabic
  7: Carboxymethyl cellulose (CMC)
  8: Gelatin
  9: Guar gum
  10: Orange peel pectin
  11: Sodium alginate + HMP

- protein_type:
  1: Fava bean protein
  2: Rice protein
  3: Pea protein
  4: Whey protein
  5: Egg white powder
  6: Cricket powder + whole milk powder
  7: White croaker surimi
  8: Casein
  9: Salmon protein isolate
  10: SPI (soy protein isolate)
  11: Whey protein fibrils

Note: The synthetic data generator (data/generate_sample_data.py) creates these coded columns and places outputs in AD, AE, AF-AI.
