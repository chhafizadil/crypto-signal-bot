import random

def analyze_market():
    # Dummy data — real implementation would analyze 2500+ Binance coins
    symbols = ['SOL/USDT', 'BTC/USDT', 'ETH/USDT']
    return {
        'symbol': random.choice(symbols),
        'side': random.choice(['BUY', 'SELL']),
        'entry': round(random.uniform(120, 150), 2),
        'tp1': round(random.uniform(110, 140), 2),
        'tp2': round(random.uniform(100, 135), 2),
        'sl': round(random.uniform(130, 160), 2),
        'volume_spike': round(random.uniform(2.5, 6.5), 1),
        'whale_activity': random.choice([True, False]),
        'news_impact': random.choice(['🟢 Positive', '🔴 Negative', '🟡 Neutral']),
        'sentiment': random.choice(['Bullish', 'Bearish', 'Neutral']),
        'trend_strength': random.choice(['Strong', 'Medium', 'Weak']),
        'timeframe': '15m, 1h, 4h',
        'recommendation': random.choice(['STRONG BUY', 'STRONG SELL']),
        'trade_type': random.choice(['Scalping', 'Normal', 'Spot']),
        'leverage': random.choice([20, 30, 50]),
        'signal_tag': f"Signal_{random.randint(1, 99)}"
    }
