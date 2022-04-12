from interface import Interface

def main():
    interface = Interface("CoinBrain", "960x540")
    interface.set_data()
    interface.set_time()
    interface.run()
    
if __name__ == "__main__":
    main()