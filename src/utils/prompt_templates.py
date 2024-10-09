from typing import Dict

class PromptTemplates:
    """Class containing prompt templates for different categories."""
    
    @staticmethod
    def get_template(category: str) -> str:
        """
        Get the prompt template for a specific category.
        
        Args:
            category: Category name (study_desk, interior, fashion)
            
        Returns:
            Template string for the category
        """
        templates = {
            'study_desk': """Given a study desk setup with the following items: {objects}
                            Please provide specific recommendations for:
                            1. Ergonomic improvements
                            2. Productivity enhancements
                            3. Aesthetic improvements
                            4. Additional items to consider
                            Make suggestions detailed and actionable.""",
            
            'interior': """In this room, I notice: {objects}
                          Please provide specific recommendations for:
                          1. Layout optimization
                          2. Color scheme improvements
                          3. Additional furniture or decor
                          4. Lighting suggestions
                          Make suggestions practical and stylish.""",
            
            'fashion': """The outfit includes: {objects}
                         Please provide specific recommendations for:
                         1. Style improvements
                         2. Complementary items
                         3. Color coordination
                         4. Accessory suggestions
                         Make suggestions trendy and practical."""
        }
        
        return templates.get(category, "")
    
    @staticmethod
    def get_system_prompt() -> str:
        """Get the system prompt for the LLM."""
        return "You are an expert interior/fashion designer providing specific recommendations."