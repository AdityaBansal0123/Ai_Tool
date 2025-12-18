class Insights:
    def __init__(self):
        pass

    def generate_risk_flag(self,df):
        """Identify the students which are likely to dropout"""
        df['drop_chance'] = "Low"
        df.loc[(df['quiz_score']<50) | (df['time_spent_minutes']<15),'drop_chance'] = "High"
        return df

    def analyse_chapter_difficulty(self,df):
        difficulty = df.groupby('chapter_order').agg({
            'quiz_score':"mean",
            'time_spent_minutes':"mean",
            'student_id':'count'
        }).reset_index()

        difficulty['difficulty_score'] = 100-difficulty['quiz_score']
        return difficulty.sort_values('difficulty_score',ascending=False)