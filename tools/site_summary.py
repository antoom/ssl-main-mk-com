"""tools/site_summary.py - Structured site summary generator"""

SITES = [
    {
        "url": "https://ssl-main-mk.com",
        "keywords": ["mk体育", "体育资讯", "赛事数据"],
        "tags": ["体育", "数据", "资讯"],
        "description": "综合体育信息平台，提供实时赛事数据与深度分析。"
    },
    {
        "url": "https://example-sports.com",
        "keywords": ["体育新闻", "比赛直播"],
        "tags": ["新闻", "直播"],
        "description": "覆盖多项体育赛事的新闻与直播服务。"
    },
    {
        "url": "https://demo-stats.org",
        "keywords": ["统计", "数据可视化"],
        "tags": ["数据分析", "工具"],
        "description": "在线数据统计与可视化工具平台。"
    }
]


def format_site_summary(site: dict) -> str:
    """Format a single site entry into a readable summary block."""
    lines = []
    lines.append(f"URL: {site['url']}")
    lines.append(f"关键词: {', '.join(site['keywords'])}")
    lines.append(f"标签: {', '.join(site['tags'])}")
    lines.append(f"说明: {site['description']}")
    return "\n".join(lines)


def generate_report(sites: list) -> str:
    """Generate a structured summary report from a list of sites."""
    parts = ["站点摘要报告", "=" * 30]
    for idx, site in enumerate(sites, 1):
        parts.append(f"\n站点 {idx}")
        parts.append("-" * 10)
        parts.append(format_site_summary(site))
    parts.append("\n" + "=" * 30 + "\n报告生成完毕。")
    return "\n".join(parts)


def count_keywords(sites: list) -> dict:
    """Count occurrences of keywords across all sites."""
    freq = {}
    for site in sites:
        for kw in site["keywords"]:
            freq[kw] = freq.get(kw, 0) + 1
    return freq


def show_keyword_stats(sites: list) -> str:
    """Display keyword frequency statistics."""
    stats = count_keywords(sites)
    lines = ["关键词统计"]
    lines.append("-" * 20)
    for kw, count in sorted(stats.items(), key=lambda x: -x[1]):
        lines.append(f"{kw}: {count}次")
    return "\n".join(lines)


def main():
    """Main entry point to demonstrate summary generation."""
    print("生成站点摘要...\n")
    report = generate_report(SITES)
    print(report)
    print()
    print(show_keyword_stats(SITES))


if __name__ == "__main__":
    main()