
def run_balance():
    # --- INPUTS ---
    soya_input = 1000.0  # kg/h
    protein_content = 0.375
    water_ratio = 12.0
    extraction_eff = 0.88
    precip_eff = 0.98
    loss_factor = 0.02  # 2% loss per stage
    okara_humidity = 0.65
    pasta_humidity = 0.50
    final_moisture = 0.05
    ro_recovery = 0.25
    evap_target_solids = 0.23

    print(f"--- BASE DE CALCULO ---")
    print(f"Soya: {soya_input} kg/h")
    print(f"Proteina entrada: {soya_input * protein_content} kg/h")
    print(f"Agua extraccion: {soya_input * water_ratio} kg/h")
    print(f"Factor de perdida operacional: {loss_factor*100}%\n")

    # --- ETAPA 1: EXTRACCION ALCALINA ---
    mass_in_e1 = soya_input + (soya_input * water_ratio)
    protein_in = soya_input * protein_content
    protein_solubilized = protein_in * extraction_eff
    
    # Applying losses to the mixture
    mass_out_e1 = mass_in_e1 * (1 - loss_factor)
    protein_out_e1 = protein_solubilized * (1 - loss_factor)
    
    print(f"ETAPA 1: Extraccion")
    print(f"  Entrada: {mass_in_e1} kg/h")
    print(f"  Salida (Lodo): {mass_out_e1} kg/h")
    print(f"  Proteina disuelta: {protein_out_e1:.2f} kg/h")

    # --- ETAPA 1.2: SEPARACION 1 (DECANTER) ---
    # Total solids in soya = soya_input (assume rest is fibre/ash for simplicity)
    # Fibre = Total Soya - Solubilized Protein
    fibre_solids = (soya_input - protein_solubilized) * (1 - loss_factor)
    
    # Okara wet mass calculation:
    # fibre_solids = okara_wet * (1 - okara_humidity)
    okara_wet = fibre_solids / (1 - okara_humidity)
    
    extract_mass = mass_out_e1 - okara_wet
    # Applying losses to extract flow
    extract_mass_net = extract_mass * (1 - loss_factor)
    protein_extract = protein_out_e1 * (1 - loss_factor)
    
    print(f"ETAPA 1.2: Separacion 1")
    print(f"  Okara humedo: {okara_wet:.2f} kg/h")
    print(f"  Extracto neto: {extract_mass_net:.2f} kg/h")
    print(f"  Proteina en extracto: {protein_extract:.2f} kg/h")

    # --- ETAPA 2: PASTEURIZACION ---
    # Mass balance: In = Out + Loss
    mass_out_e2 = extract_mass_net * (1 - loss_factor)
    protein_out_e2 = protein_extract * (1 - loss_factor)
    
    print(f"ETAPA 2: Pasteurizacion")
    print(f"  Salida: {mass_out_e2:.2f} kg/h")
    print(f"  Proteina: {protein_out_e2:.2f} kg/h")

    # --- ETAPA 2.5: OSMOSIS INVERSA ---
    water_removed_ro = mass_out_e2 * ro_recovery
    retentate_ro = mass_out_e2 - water_removed_ro
    # Applying losses to retentate
    retentate_net = retentate_ro * (1 - loss_factor)
    protein_ro = protein_out_e2 * (1 - loss_factor)
    
    print(f"ETAPA 2.5: Osmosis Inversa")
    print(f"  Agua removida (Permeado): {water_removed_ro:.2f} kg/h")
    print(f"  Retentado neto: {retentate_net:.2f} kg/h")
    print(f"  Proteina: {protein_ro:.2f} kg/h")

    # --- ETAPA 3: EVAPORACION ---
    # Target 23% solids. 
    # Current solids = protein_ro + small amount of other things (let's assume only protein for simplicity)
    # Actually, let's keep track of "total solids" more carefully.
    solids_e3 = protein_ro # Simplified
    concentrate_mass = solids_e3 / evap_target_solids
    water_evap = retentate_net - concentrate_mass
    # Applying losses to concentrate
    concentrate_net = concentrate_mass * (1 - loss_factor)
    protein_evap = protein_ro * (1 - loss_factor)

    print(f"ETAPA 3: Evaporacion")
    print(f"  Agua evaporada: {water_evap:.2f} kg/h")
    print(f"  Concentrado neto: {concentrate_net:.2f} kg/h")
    print(f"  Proteina: {protein_evap:.2f} kg/h")

    # --- ETAPA 4: PRECIPITACION & SEPARACION 2 ---
    protein_precipitated = protein_evap * precip_eff
    # Pasta wet mass: protein_precipitated = pasta_wet * (1 - pasta_humidity)
    pasta_wet = protein_precipitated / (1 - pasta_humidity)
    whey_mass = concentrate_net - pasta_wet
    
    # Applying losses to pasta
    pasta_net = pasta_wet * (1 - loss_factor)
    protein_pasta = protein_precipitated * (1 - loss_factor)
    
    print(f"ETAPA 4: Precipitacion y Separacion 2")
    print(f"  Pasta humeda neta: {pasta_net:.2f} kg/h")
    print(f"  Suero residual: {whey_mass:.2f} kg/h")
    print(f"  Proteina en pasta: {protein_pasta:.2f} kg/h")

    # --- ETAPA 5: SECADO SPRAY ---
    # Final product: protein_pasta / (1 - final_moisture)
    powder_mass = protein_pasta / (1 - final_moisture)
    water_removed_spray = pasta_net - powder_mass
    # Final losses in packaging/powder recovery
    powder_net = powder_mass * (1 - loss_factor)
    protein_final = protein_pasta * (1 - loss_factor)
    
    print(f"ETAPA 5: Secado Spray")
    print(f"  Agua removida: {water_removed_spray:.2f} kg/h")
    print(f"  Polvo final neto: {powder_net:.2f} kg/h")
    print(f"  Proteina final neta: {protein_final:.2f} kg/h")
    print(f"  Pureza: {(protein_final/powder_net)*100:.2f}%")
    print(f"  Rendimiento global proteina: {(protein_final/(soya_input*protein_content))*100:.2f}%")

if __name__ == "__main__":
    run_balance()
