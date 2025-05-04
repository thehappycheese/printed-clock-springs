from sympy import sqrt, pi, ln

def spiral_length_truncated(radius_inner:float, radius_outer:float, turns:float):
    radius_diff = radius_outer-radius_inner
    all_turns = radius_outer/radius_diff * turns
    small_turns = radius_inner/radius_diff * turns
    angle_from = small_turns * pi*2
    angle_to   = all_turns   * pi*2
    b=radius_outer / all_turns / pi/2
    return spiral_length(b,angle_from, angle_to)

def spiral_length(b,t1,t2):
    """
    b: increase in radius per radian
    t1:start angle in radians
    t2:end angle in radians
    """
    def pog(t):
        f = sqrt(1+t**2)
        return t*f + ln(t + f)
    
    leng = b/2*(pog(t2)-pog(t1))
    return leng


def spring_active_length(radius_inner:float, radius_outer:float, turns:float):
    """
    Calculate the active length of a flat spiral spring.
    
    Parameters:
    inner_radius: Inner radius of the spring in meters
    outer_radius: Outer radius of the spring in meters
    turns: Number of turns in the spring
    """
    return  spiral_length_truncated(radius_inner, radius_outer, turns)

def spring_constant(youngs_modulus, width, thickness, length):
    """
    Calculate the spring constant (k) for a flat spiral spring.
    
    Parameters:
    youngs_modulus (float): Young's modulus of the material in Pa
    width (float): Width of the spring strip in meters
    thickness (float): Thickness of the spring strip in meters
    length (float): Active length of the spring in meters
    
    Returns:
    float: Spring constant k in N·m/rad
    """
    return (youngs_modulus * width * thickness**3) / (12 * length)