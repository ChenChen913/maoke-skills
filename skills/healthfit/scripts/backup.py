#!/usr/bin/env python3
"""
HealthFit 数据备份脚本
功能：备份 data/ 目录到 data/db/backup/
"""

import os
import shutil
import json
from datetime import datetime
from pathlib import Path

def get_skill_dir():
    """获取 HealthFit skill 根目录"""
    return Path(__file__).parent.parent

def get_data_dir():
    """获取 data 目录"""
    return get_skill_dir() / "data"

def get_backup_dir():
    """获取备份目录"""
    return get_skill_dir() / "data" / "db" / "backup"

def create_backup():
    """创建数据备份"""
    data_dir = get_data_dir()
    backup_dir = get_backup_dir()
    
    # 确保备份目录存在
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    # 生成备份文件名（带时间戳）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    backup_path = backup_dir / backup_name
    
    # 复制 data 目录（排除 backup 目录本身）
    print(f"开始备份数据到：{backup_path}")
    
    # 创建备份目录结构
    backup_path.mkdir(parents=True, exist_ok=True)
    
    # 复制 json 目录
    json_dir = data_dir / "json"
    if json_dir.exists():
        shutil.copytree(json_dir, backup_path / "json")
        print(f"✓ 已备份 JSON 数据")
    
    # 复制 txt 目录
    txt_dir = data_dir / "txt"
    if txt_dir.exists():
        shutil.copytree(txt_dir, backup_path / "txt")
        print(f"✓ 已备份 TXT 日志")
    
    # 复制 db 文件（排除 backup 目录）
    db_dir = data_dir / "db"
    if db_dir.exists():
        db_backup_dir = backup_path / "db"
        db_backup_dir.mkdir(exist_ok=True)
        for db_file in db_dir.glob("*.db"):
            shutil.copy2(db_file, db_backup_dir / db_file.name)
        print(f"✓ 已备份 SQLite 数据库")
    
    # 生成备份清单
    manifest = {
        "backup_time": timestamp,
        "backup_path": str(backup_path),
        "files": {
            "json": len(list((backup_path / "json").glob("*.json"))) if (backup_path / "json").exists() else 0,
            "txt": len(list((backup_path / "txt").glob("*.txt"))) if (backup_path / "txt").exists() else 0,
            "db": len(list((backup_path / "db").glob("*.db"))) if (backup_path / "db").exists() else 0
        }
    }
    
    with open(backup_path / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 备份完成：{backup_path}")
    print(f"  - JSON 文件：{manifest['files']['json']} 个")
    print(f"  - TXT 文件：{manifest['files']['txt']} 个")
    print(f"  - DB 文件：{manifest['files']['db']} 个")
    
    return backup_path

def cleanup_old_backups(keep_count=4):
    """清理旧备份，保留最近 N 个"""
    backup_dir = get_backup_dir()
    
    if not backup_dir.exists():
        return
    
    # 获取所有备份目录，按时间排序
    backups = sorted([d for d in backup_dir.iterdir() if d.is_dir()], reverse=True)
    
    # 删除超出保留数量的旧备份
    if len(backups) > keep_count:
        for old_backup in backups[keep_count:]:
            print(f"删除旧备份：{old_backup}")
            shutil.rmtree(old_backup)

if __name__ == "__main__":
    print("🔵 HealthFit 数据备份工具")
    print("=" * 50)
    
    try:
        backup_path = create_backup()
        cleanup_old_backups(keep_count=4)
        print("=" * 50)
        print("✅ 备份完成！")
    except Exception as e:
        print(f"❌ 备份失败：{e}")
        raise
