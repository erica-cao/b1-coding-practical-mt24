class PDController:
    def __init__(self, K_P: float, K_D: float):
        self.K_P = K_P
        self.K_D = K_D
        self.prev_error = 0  # Initialize previous error for derivative calculation

    def compute_control(self, reference: float, current_depth: float):
        # Calculate the error
        error = reference - current_depth
        
        # Proportional term
        proportional = self.K_P * error
        
        # Derivative term (change in error)
        derivative = self.K_D * (error - self.prev_error)
        
        # Control action
        control_action = proportional + derivative
        
        # Update previous error
        self.prev_error = error
        
        return control_action
