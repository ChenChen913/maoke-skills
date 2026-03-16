#!/usr/bin/env python3
"""
HealthFit 数据导出脚本
功能：将 JSON/TXT/SQLite 数据导出为 Markdown 报告
"""

import os
import json
from datetime import datetime
from pathlib import Path

def get_skill_dir():
    """获取 HealthFit skill 根目录"""
    return Path(__file__).parent.parent

def get_data_dir():
    """获取 data 目录"""
    return get_skill_dir() / "data"

def get_export_dir():
    """获取导出目录"""
    return get_skill_dir() / "exports"

def load_json(file_path):
    """加载 JSON 文件"""
    if not file_path.exists():
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def export_profile():
    """导出用户档案"""
    profile = load_json(get_data_dir() / "json" / "profile.json")
    if not profile or not profile.get("nickname"):
        return "## 用户档案\n\n暂无数据（请先完成建档）\n"
    
    md = "## 用户档案\n\n"
    md += f"- **昵称：** {profile.get('nickname', '未设置')}\n"
    md += f"- **性别：** {profile.get('gender', '未设置')}\n"
    md += f"- **年龄：** {profile.get('age', '未设置')}\n"
    md += f"- **身高：** {profile.get('height_cm', '未设置')} cm\n"
    md += f"- **体重：** {profile.get('weight_kg', '未设置')} kg\n"
    md += f"- **体脂率：** {profile.get('body_fat_pct', '未设置')}%\n"
    md += f"- **BMI：** {profile.get('bmi', '未设置')}\n"
    md += f"- **目标：** {profile.get('primary_goal', '未设置')}\n"
    md += f"- **目标体重：** {profile.get('target_weight_kg', '未设置')} kg\n"
    return md + "\n"

def export_tcm_profile():
    """导出中医体质档案"""
    tcm = load_json(get_data_dir() / "json" / "tcm_profile.json")
    if not tcm or not tcm.get("primary_constitution"):
        return "## 中医体质档案\n\n暂无数据（请先完成体质辨识）\n"
    
    md = "## 中医体质档案\n\n"
    md += f"- **主体质：** {tcm.get('primary_constitution', '未设置')}\n"
    md += f"- **兼夹体质：** {', '.join(tcm.get('secondary_constitutions', [])) or '无'}\n"
    md += f"- **辨识日期：** {tcm.get('created_at', '未设置')}\n"
    md += f"- **最近复查：** {tcm.get('last_assessed', '未设置')}\n"
    
    # 舌象记录
    tongue_records = tcm.get("tongue_records", [])
    if tongue_records:
        md += "\n### 舌象记录\n\n"
        for record in tongue_records[-3:]:  # 最近 3 次
            md += f"- **{record.get('date')}**: {record.get('body_color')} {record.get('body_shape')}，{record.get('coating')}\n"
    
    return md + "\n"

def export_daily_logs():
    """导出每日日志摘要"""
    daily_dir = get_data_dir() / "json" / "daily"
    if not daily_dir.exists():
        return "## 每日日志\n\n暂无数据\n"
    
    # 获取最近 7 天的日志
    logs = sorted(daily_dir.glob("*.json"), reverse=True)[:7]
    
    md = "## 最近 7 天日志\n\n"
    for log_file in logs:
        data = load_json(log_file)
        if not data:
            continue
        
        date = log_file.stem
        md += f"### {date}\n\n"
        
        # 身体指标
        metrics = data.get("metrics", {})
        if metrics.get("weight_kg"):
            md += f"- **体重：** {metrics['weight_kg']} kg\n"
        if metrics.get("sleep_hours"):
            md += f"- **睡眠：** {metrics['sleep_hours']} 小时\n"
        if metrics.get("energy_level"):
            md += f"- **精力：** {metrics['energy_level']}/10\n"
        
        # 运动
        workout_ids = data.get("workout_ids", [])
        if workout_ids:
            md += f"- **运动：** {len(workout_ids)} 次\n"
        
        md += "\n"
    
    return md

def export_achievements():
    """导出成就记录"""
    achievements_file = get_data_dir() / "txt" / "achievements.txt"
    if not achievements_file.exists():
        return "## 成就记录\n\n暂无成就\n"
    
    with open(achievements_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 过滤掉注释和空行
    lines = [line for line in content.split("\n") if line.strip() and not line.startswith("#")]
    
    if len(lines) <= 1:
        return "## 成就记录\n\n暂无成就\n"
    
    return "## 成就记录\n\n" + "\n".join(lines) + "\n"

def generate_full_report():
    """生成完整导出报告"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    md = f"# HealthFit 健康数据导出报告\n\n"
    md += f"**导出时间：** {timestamp}\n\n"
    md += "---\n\n"
    
    # 导出各模块
    md += export_profile()
    md += "---\n\n"
    md += export_tcm_profile()
    md += "---\n\n"
    md += export_daily_logs()
    md += "---\n\n"
    md += export_achievements()
    
    return md

def main():
    """主函数"""
    print("🔵 HealthFit 数据导出工具")
    print("=" * 50)
    
    # 确保导出目录存在
    export_dir = get_export_dir()
    export_dir.mkdir(parents=True, exist_ok=True)
    
    # 生成报告
    print("正在生成导出报告...")
    report = generate_full_report()
    
    # 保存报告
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = export_dir / f"export_{timestamp}.md"
    
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"✓ 报告已导出：{report_file}")
    print("=" * 50)
    print("✅ 导出完成！")
    
    return report_file

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ 导出失败：{e}")
        raise
