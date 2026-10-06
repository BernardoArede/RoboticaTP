from pathlib import Path

import yaml


DEFAULT_CONFIG = (
    Path(__file__).resolve().parent.parent / "config" / "robot.yaml"
)

def load_config(path=DEFAULT_CONFIG):
    with Path(path).open("r", encoding="utf-8-sig") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError("A configuração deve ser um dicionário.")

    robot = config.get("robot")
    if not isinstance(robot, dict):
        raise ValueError("Falta a secção 'robot'.")

    if robot.get("angle_unit") not in ("degree", "radian"):
        raise ValueError("angle_unit deve ser 'degree' ou 'radian'.")

    return config