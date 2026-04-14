---
lang: en
title: "10.8. Elec_Mag Data"
---

# 10.8. Electrical and Magnetic Data

Electrical and magnetic properties (See Fig. 10.8.1.) are input here if electrical or electromagnetic behaviors are to be modeled in an object.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_8_Elec_Mag_Data/10_8_Image001.jpg)

Electric and Magnetic material data window

## Electrical resistivity (ELRST)

Electrical resistance is the measure for how a given material opposes (resists) electrical current flow over an applied voltage difference. Electrical resistivity ([ELRST](/docs/en/Keyword_Documentation/E/ELRST/)) is the amount of electrical resistance per unit length for a given material. The value can be a constant or a function of temperature, a function of atom content, or a function of temperature and atom content.

Electrical resistivity data is required when modeling current flow in resistance heating, spot welding, electrical upsetting, induction heating/hardening and electro-magnetic forming.

## Relative magnetic permeability (PMEAB)

Relative magnetic permeability ([PMEAB](/docs/en/Keyword_Documentation/P/PMEAB/)) is the measure for how a given material increases or decreases the density of magnetic flux lines in a volume as compared to that of a vacuum. It can be calculated by dividing the permeability of the object by the permeability of a vacuum. The dimensionless ratio should be the same in the English and SI unit systems. The value can be a constant or a function of temperature, a function of density, or a function of temperature and magnetic field intensity.

Relative magnetic permeability data is required when modeling magnetic fields in induction heating/hardening and electro-magnetic forming.

Relative magnetic permeability of many metals has been shown to be a function of temperature and magnetic field intensity. Materials are often described by their initial and/or maximum relative magnetic permeability values. The relative magnetic permeability of a magnetic material (low carbon steel, alloy steel, etc.) falls to 1 at the metal’s Curie point, which is the temperature where the metal loses its magnetization. Nonmagnetic materials (copper, aluminum, etc.) and magnetic materials above the Curie point will have a relative magnetic permeability around 1. Relative magnetic permeability typically decreases toward 1 as magnetic field intensity increases.

The permeability of a vacuum ([ENVMPR](/docs/en/Keyword_Documentation/E/ENVMPR/)) is defined in the Simulation Controls > Process Conditions menu. The typical value is provided below for reference.

1.26 x 10-9 H/mm (SI)  
3.20 x 10-8 H/in (English)

## Relative electric permittivity (PMITT)

Relative electric permittivity ([PMITT](/docs/en/Keyword_Documentation/P/PMITT/)) is the electrical polarizability of a material compared to that of a vacuum. It can be calculated by dividing the permittivity of the object by the permittivity of a vacuum. The dimensionless ratio should be the same in the English and SI unit systems. The value can be a constant, a function of temperature, or a function of density. A value of 0 (ignored) or 1 (identical to a vacuum) is typically recommended.

Relative electric permittivity is available but seldom used.

The permittivity of a vacuum ([ENVMPT](/docs/en/Keyword_Documentation/E/ENVMPT/)) is defined in the Simulation Controls > Process Conditions menu. The typical value is provided below for reference.

8.85 x 10-15 F/mm (SI)   
2.25 x 10-13 F/in (English)
