import sys
sys.path.append("/home/robert/c24git/BerryPick/BerryPicker/used_gits/Conv-VAE-PyTorch")
print("Vision-based robot manipulator.\n v0.1.2 Aug 26, 2024, Lotzi Bölöni\n")

print("1. Collect demonstrations interactively")
print("2. View and annotate demonstrations")
print("3. Replay demonstrations on the robot")
print("4. Learn representations")
print("5. Preprocess representations")
print("6. Learn motion controller / robot policy")
print("7. Run the robot")

choice = int(input("Choose desired action: "))

if choice == 1: # Collect demonstrations interactively, robot moves on random path and camera takes pictures
    import cmd_demonstration_collector
    cmd_demonstration_collector.main()
    sys.exit(0)
if choice == 2: # View and annotate demonstrations collected in the previous step
    import cmd_demonstration_viewer
    cmd_demonstration_viewer.main()
    sys.exit(0)
if choice == 3: # Replay demonstrations on the robot
    import cmd_demonstration_replay
    cmd_demonstration_replay.main()
    sys.exit(0)
if choice == 4: # Learn representations that can be found in train folder
    import cmd_learn_representation
    cmd_learn_representation.main()
    sys.exit(0)
if choice == 5: # Preprocess representations Not fully implemented yet
    import cmd_preprocess_representation
    cmd_preprocess_representation.main()
    sys.exit(0)
if choice == 6: # Learn motion controller / robot policy NOT IMPLEMENTED YET
    import cmd_learn_motion_controller
    cmd_learn_motion_controller.main()
    sys.exit(0)
if choice == 7: # Run the robot, steps 1-4 must be completed before this step
    import cmd_run_robot
    cmd_run_robot.main()
    sys.exit(0)

print(f"There is no such command {choice}!")