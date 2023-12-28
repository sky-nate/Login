import rlgym

env = rlgym.make()
game_speed: int = 100

tick_skip: int = 8

spawn_opponents: bool = True

self_play: bool = False

random_resets: bool = False

eam_size: int = 1

terminal_conditions: List[object] = (TimeoutCondition(225), GoalScoredCondition())

reward_fn: object = DefaultReward()

obs_builder: object = DefaultObs()

action_parser: object = DefaultAction()

state_setter: object = DefaultState()

launch_preference: str = LaunchPreference.EPIC

path_to_rl: str = None

use_injector: bool = False

force_paging: bool = False