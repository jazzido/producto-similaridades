# Similaridad de nombres de productos (PoC para mgaitan/preciosa]

## Instalación

  - Dependencias
    ``` pip install -r requirements.txt`
  - Cargar datos
    ```
    python load_data.py productos.json
    ```
  - Crear indice *trigram* en la DB:
    ```
    CREATE EXTENSION pg_trgm;
    CREATE INDEX descripcion_trgm_idx ON productos_preciosa USING gist (descripcion gist_trgm_ops);
    ```

## Probando:

`sml.py` acepta un argumento `descripcion`. Imprime una lista de candidatos en `STDOUT` (descripcion, indice de similaridad)


```
$ python sml.py "Cloro HTH CLOROTEC shock bal 4 kg"
Productos similares a `Cloro HTH CLOROTEC shock bal 4 kg`:

Cloro shock clorotec 4kg		0.5806
Cloro shock clorotec 1kg		0.5312
Cloro fresclor shock 1 kg		0.3947
Cloro granulado clorotec 1 kg		0.3171
```

```
python sml.py "Milanesas de soja MONDO FRIZZATTA ceb/que  cja 380 grm"
Productos similares a `Milanesas de soja MONDO FRIZZATTA ceb/que  cja 380 grm`:

Mondo Frizzatta - Cebolla y Queso Milanesa de soja rellenas con cebolla y queso. Congelado. 4 unidades. 380 Grs		0.4783
Mondo Frizzatta - Choclo y Queso Milanesa de soja rellenas con choclo y queso. Congelado. 4 unidades. 380 Grs		0.4516
Mondo Frizzatta - Jamón y Queso Milanesa de soja rellenas con jamó y queso. Congelado. 4 unidades. 380 Grs		0.4468
Mondo Frizzatta - Tomate y Queso Milanesa de soja rellenas con tomate y queso. Congelado. 4 unidades. 380 Grs		0.4468
Mondo Frizzatta - Espinaca y Queso Milanesa de soja rellenas con espinaca y queso. Congelado. 4 unidades. 380 Grs		0.4375
Milanesa de soja jamon & queso mf 380gr		0.3538
Milanesa de soja jamon y queso swift 380gr		0.3286
Milanesas de soja finca natural 340 gr		0.3235
Milanesa de soja espinaca & queso mf 380gr		0.3188
Mondo Frizzatta - Medallones de merluza Congelado. 300 Grs		0.3038
```
