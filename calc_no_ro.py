
def run_balance_no_ro():
    soya_input = 1000.0  # kg/h
    protein_content = 0.375
    water_ratio = 12.0
    extraction_eff = 0.88
    precip_eff = 0.98
    loss_factor = 0.02
    okara_humidity = 0.65
    pasta_humidity = 0.50
    final_moisture = 0.05
    evap_target_solids = 0.23

    print(f"--- BASE DE CALCULO ---")
    
    # E1
    mass_in_e1 = soya_input + (soya_input * water_ratio)
    protein_solubilized = (soya_input * protein_content) * extraction_eff
    mass_out_e1 = mass_in_e1 * (1 - loss_factor)
    protein_out_e1 = protein_solubilized * (1 - loss_factor)
    
    # E1.2
    fibre_solids = (soya_input - protein_solubilized) * (1 - loss_factor)
    okara_wet = fibre_solids / (1 - okara_humidity)
    extract_mass = mass_out_e1 - okara_wet
    extract_mass_net = extract_mass * (1 - loss_factor)
    protein_extract = protein_out_e1 * (1 - loss_factor)
    
    # E2
    mass_out_e2 = extract_mass_net * (1 - loss_factor)
    protein_out_e2 = protein_extract * (1 - loss_factor)
    
    # E3 (NO RO)
    solids_e3 = protein_out_e2
    concentrate_mass = solids_e3 / evap_target_solids
    water_evap = mass_out_e2 - concentrate_mass
    concentrate_net = concentrate_mass * (1 - loss_factor)
    protein_evap = protein_out_e2 * (1 - loss_factor)
    
    # E4
    protein_precipitated = protein_evap * precip_eff
    pasta_wet = protein_precipitated / (1 - pasta_humidity)
    whey_mass = concentrate_net - pasta_wet
    pasta_net = pasta_wet * (1 - loss_factor)
    protein_pasta = protein_precipitated * (1 - loss_factor)
    
    # E5
    powder_mass = protein_pasta / (1 - final_moisture)
    water_removed_spray = pasta_net - powder_mass
    powder_net = powder_mass * (1 - loss_factor)
    protein_final = protein_pasta * (1 - loss_factor)
    
    print(f"ETAPA 2 (Salida Pasteurizacion)")
    print(f"  Salida: {mass_out_e2:.2f} kg/h")
    print(f"  Proteina: {protein_out_e2:.2f} kg/h")
    
    print(f"ETAPA 3 (Evaporacion Directa)")
    print(f"  Agua evaporada: {water_evap:.2f} kg/h")
    print(f"  Concentrado neto: {concentrate_net:.2f} kg/h")
    print(f"  Proteina: {protein_evap:.2f} kg/h")
    
    print(f"ETAPA 4 (Precipitacion y Centrifugacion)")
    print(f"  Pasta humeda neta: {pasta_net:.2f} kg/h")
    print(f"  Suero residual: {whey_mass:.2f} kg/h")
    print(f"  Proteina en pasta: {protein_pasta:.2f} kg/h")
    
    print(f"ETAPA 5 (Secado Spray)")
    print(f"  Agua removida: {water_removed_spray:.2f} kg/h")
    print(f"  Polvo final neto: {powder_net:.2f} kg/h")
    print(f"  Proteina final neta: {protein_final:.2f} kg/h")
    
    print(f"\n--- VERIFICACION GLOBAL ---")
    mermas_acumuladas = (
        (mass_in_e1 * loss_factor) + # e1
        (extract_mass * loss_factor) + # e1.2
        (extract_mass_net * loss_factor) + # e2
        (concentrate_mass * loss_factor) + # e3
        (pasta_wet * loss_factor) + # e4
        (powder_mass * loss_factor) # e5
    )
    print(f"Mermas operacionales acumuladas: {mermas_acumuladas:.2f} kg/h")
    total_out = okara_wet + water_evap + whey_mass + powder_net + water_removed_spray + mermas_acumuladas
    print(f"Suma Salidas + Mermas: {total_out:.2f} kg/h")

run_balance_no_ro()
