def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("Flavor not recognized")
    except ValueError as e:
        print(f"Error:" , e)
    else:
        print(f"{flavor} chai is ready!")
    finally:
        print("Next order please!")

serve_chai("masala")
serve_chai("unknown")