
model_name='TS2Vec'
root_path='/home/schaffen/Workspace/Project/TS2Vec/'

python -u run.py \
    --training True \
    --model TS2Vec \
    --seed 2021 \
    --root_path $root_path \
    --checkpoints ./checkpoints/ \
    --data_path data/XAUUSD_M5.csv \
    --target CandleType \
    --time_feature Time \
    --gpu True \
    --device 0