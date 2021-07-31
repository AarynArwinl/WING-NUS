from pathlib import Path
BASE_DIR = Path('pybert')

# configs corresponds to be provided files in the drive
config = {
    'model_weight': '1JT24Jq-5M2W5Tq8zdm8WwFLIExmbzFYJ',
    'model_config': '1l55bByNdu6b4soNDhn2ZLHXttYVS8EUn',
    'model_checkpoint': '1mhYxj7DEDgGeYWxed_sgYtJyZQPEuHSo',

    'sample_test_set': '1nMDmxqEhRBKBJKpbK33GVHq_TSGCs7FX', 
    'sample_train_set': '1jwrWYnAuUn2d-ljAJ6vbpwMCy_sYEMDu',
    'sample_valid_set': '1YbrxClsy00RP_pkkjs4xL33llS82R3Hn'
}

file_path = {
    'model_weight': BASE_DIR / 'pretrain/bert/bert-uncased/pytorch_model.bin',  
    'model_config': BASE_DIR / 'pretrain/bert/bert-uncased/config.json',  
    'model_checkpoint': BASE_DIR / 'pretrain/bert/bert-uncased/checkpoint_info.bin',  

    'sample_test_set': BASE_DIR / 'dataset/job_dataset.test.pkl',
    'sample_train_set': BASE_DIR / 'dataset/job_dataset.train.pkl',
    'sample_valid_set': BASE_DIR / 'dataset/job_dataset.valid.pkl'
}   